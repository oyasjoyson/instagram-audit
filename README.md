# Audit — Instagram follower analysis

A small client-side tool to quickly find who doesn't follow you back on Instagram using your official Instagram data export. Everything runs in your browser — no files are uploaded to a server and your data stays private.

## Quick summary

- Purpose: Compare your Instagram followers and following lists and surface accounts that don't follow you back, mutuals, blocked profiles, and diffs between exports.
- Privacy: All processing happens locally in the browser (no network requests or servers).
- Run: Open `insta.html` in a modern browser and follow the on-page instructions to upload your exported JSON files.

## Features

- Parse Instagram "Followers" export (followers_*.json — Instagram may split the export into numbered files).
- Parse Instagram "Following" export (following.json).
- Optional: parse `blocked_profiles.json` to highlight blocked accounts.
- Show counts: following, followers, not-following-back.
- List users with quick links to profiles (if present in the export).
- Works fully offline in the browser.

## How to use

1. Get your Instagram data export:
   - Instagram → Settings → Accounts Center → Your information and permissions → Download your information.
   - Select "Followers and following" and choose JSON format.
   - Instagram may generate multiple follower files (e.g., `followers_1.json`, `followers_2.json`, ...). Download them all.

2. Open the tool:
   - Option A: Double-click `insta.html` to open it in your default browser.
   - Option B (recommended if the browser restricts file access): Serve the folder with a simple static server, e.g.:
     - Python 3: `python -m http.server 8000` and visit `http://localhost:8000/insta.html`
     - Or any static file server.

3. Upload files:
   - Use the "Followers" dropzone to select all `followers_*.json` files.
   - Use the "Following" dropzone to select `following.json`.
   - (Optional) Use the "Blocked profiles" dropzone to select `blocked_profiles.json`.

4. Click the Analyze / Start button (on the page) and review results.

## Supported files / expected file names

- followers_*.json — Instagram splits followers exports into one or more files.
- following.json — list of accounts you follow.
- blocked_profiles.json — optional list of blocked accounts.

The tool expects the JSON format produced by Instagram's official export. If Instagram changes their export format, parsing may fail.

## Privacy & Security

- The app is purely client-side. Files are read in the browser using the File API and processed locally.
- No data leaves your device — there are no network requests for uploaded files.
- Do not share sensitive files publicly. If you want to share results, export only the minimal information necessary.

## Browser compatibility

- Modern Chromium-based browsers, Firefox, and Safari should work.
- If the page appears blank or file selection fails, try serving the file over `http://localhost` (some browsers limit File API access for `file://` contexts).

## Development

- The UI and logic are contained in `insta.html`.
- To iterate locally:
  1. Make changes to `insta.html`.
  2. Open it in the browser or serve via a local static server.
- If you want to split JS/CSS into separate files or add a build pipeline, you can extract the embedded <style> and <script> blocks and add a bundler or plain static layout.

## Troubleshooting

- "Counts are lower than expected": Make sure you selected all `followers_*.json` files from your export. Instagram often splits followers across several files.
- "Nothing happens when I upload": Check browser console for errors. Try serving the file via a local server instead of opening `file://`.
- "Profile links missing": Instagram export JSON contains limited profile metadata. The tool uses whatever is present in your export.

## Contribution & customization

- Contributions welcome. Keep in mind the privacy-first design: avoid adding features that send raw data to external servers unless explicitly opt-in and documented.
- If you'd like, I can:
  - Extract JS into a separate file.
  - Add a small export CSV/JSON option that contains only usernames and minimal metadata.
  - Add automated tests for parsing logic.

## License

MIT — see LICENSE (or add one if you want).

## Author

Original HTML file in this repository (author: @oyasjoyson)
