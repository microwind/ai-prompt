# Repository Guidelines

## Project Structure & Module Organization
- Core guides live in `README.md`, `README_EN.md`, `programmer_prompt_engineering_guide.md`, and `developer_prompt_engineering_guide.md`.
- Fourteen task playbooks sit in `01-Requirement-Clarification` … `14-Documentation-Generation`, each with a `README.md` (and occasional checklists/examples). Keep new task folders numbered with two digits and kebab-case names.
- Scenario libraries: `Prompt-Examples/` holds domain examples (content, system design, data, code); `Prompt-Frameworks/` stores framework cheat-sheets (CRISPE, RTF, etc.).
- Quick navigation lives in `QUICK-REFERENCE.md` and `项目完整导航.md`; archive stale material under `_ARCHIVE/` rather than deleting.

## Build, Test, and Development Commands
- No build toolchain is required; the repo is Markdown-first.
- Recommended checks before pushing:
  - `git status` to confirm only intended files change.
  - `rg "TODO|🔄"` to catch unfinished placeholders.
  - Optional: `npx markdownlint "**/*.md"` if you have markdownlint globally; align with default rules (no custom config yet).

## Coding Style & Naming Conventions
- Write in concise Markdown; start each file with a single `#` title that matches the page purpose (bilingual titles are welcome, e.g., `T01: Requirement Clarification（需求澄清）`).
- Prefer short paragraphs, ordered lists for steps, and tables/checklists for prompts. Use fenced code blocks with language tags for prompts or command samples.
- File/dir names: lowercase kebab-case; keep numeric prefixes for task folders and sequential examples (e.g., `01-Content-Generation/01-Entertainment/03-tv-series-summary.md`).
- Emojis ✅/🔄 are used to signal status in catalogs; keep that convention when adding new entries.

## Testing Guidelines
- There is no automated test suite; perform manual checks: preview Markdown, verify internal links, and ensure code blocks or prompts render correctly in common viewers (GitHub, mdbook style).
- For new prompts, run them once against your target model to confirm the instruction flow and expected outputs; capture a minimal example if helpful.

## Commit & Pull Request Guidelines
- Commit messages in history are short and imperative (e.g., `update readme`). Follow that style; keep under ~72 characters and mention scope when useful (e.g., `update prompt examples`).
- PRs should include: one-paragraph summary, key files touched, a note on placeholders left (`🔄`), and—when changing prompt outputs—before/after samples or screenshots of rendered Markdown.
- Link issues if applicable and confirm you ran the checks above; avoid bundling unrelated docs in the same PR.

## Security & Content Hygiene
- Do not commit proprietary data, API keys, or user-identifiable examples. Use neutral or fictitious sample data and placeholders like `YOUR_API_KEY`.
- Keep the repo UTF-8/ASCII friendly; avoid smart quotes and full-width punctuation inside code fences.
