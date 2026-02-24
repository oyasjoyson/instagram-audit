import json
import streamlit as st


def extract_usernames(data_list):
    usernames = set()

    for item in data_list:
        if not isinstance(item, dict):
            continue

        # Primary Instagram format
        string_data = item.get("string_list_data", [])
        if isinstance(string_data, list) and string_data:
            value = string_data[0].get("value")
            if value:
                usernames.add(value.strip())
                continue

        # Fallback format
        title = item.get("title")
        if title:
            usernames.add(title.strip())

    return usernames


def load_json(uploaded_file):
    try:
        return json.loads(uploaded_file.read().decode("utf-8"))
    except Exception as e:
        st.error(f"❌ Failed to read {uploaded_file.name}: {e}")
        return None


def normalize_instagram_data(data, key_name):
    """
    Handles ALL Instagram JSON formats:
    - dict -> key -> list
    - dict -> key -> { data: [...] }
    - list directly
    """
    if isinstance(data, dict):
        value = data.get(key_name, [])
        if isinstance(value, dict):
            return value.get("data", [])
        if isinstance(value, list):
            return value
        return []

    if isinstance(data, list):
        return data

    return []


st.title("📊 Instagram Followers Audit Tool")
st.write("Upload your Instagram export JSON files below.")

# Upload followers files (multiple)
followers_files = st.file_uploader(
    "Upload followers JSON file(s)",
    type=["json"],
    accept_multiple_files=True
)

# Upload following file
following_file = st.file_uploader(
    "Upload following.json",
    type=["json"]
)

if followers_files and following_file:

    followers = set()
    following = set()

    # Process followers files
    for file in followers_files:
        data = load_json(file)
        if not data:
            continue

        followers_data = normalize_instagram_data(
            data, "relationships_followers"
        )
        followers.update(extract_usernames(followers_data))

    # Process following file
    data = load_json(following_file)
    if data:
        following_data = normalize_instagram_data(
            data, "relationships_following"
        )
        following.update(extract_usernames(following_data))

    # Compute differences
    not_following_back = sorted(following - followers)
    fans_only = sorted(followers - following)

    st.success("✅ Audit Complete!")

    st.subheader(f"Total Following: {len(following)}")
    st.subheader(f"Total Followers: {len(followers)}")

    st.divider()

    st.subheader(f"❌ Not Following You Back ({len(not_following_back)})")
    st.write(not_following_back)

    st.divider()

    st.subheader(f"⭐ Follow You But You Don't Follow Back ({len(fans_only)})")
    st.write(fans_only)

    # Download buttons
    st.download_button(
        "Download Not Following Back",
        "\n".join(not_following_back),
        file_name="not_following_back.txt"
    )

    st.download_button(
        "Download Fans Only",
        "\n".join(fans_only),
        file_name="fans_only.txt"
    )