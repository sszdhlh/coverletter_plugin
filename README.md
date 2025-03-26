你遇到的错误提示是：

```
Error in user YAML: (<unknown>): found character that cannot start any token while scanning for the next token at line 1 column 1
```

这是因为你试图将整个 Markdown 内容（含 `markdown` 代码块语法 ```markdown）复制进了 GitHub 上某个 YAML 格式的地方（比如 GitHub Actions、`.github/workflows/*.yml`、或者其他 `.yml` 文件中），YAML 不支持这种 Markdown 风格的代码块，会报错。

---

### ✅ 解决方法：

你只需要**去掉外层的 Markdown 标记**（最上面的 ```markdown 和最后的 ```）再粘贴就可以正常用在 `README.md` 文件中。

---

### ✂️ 修正版本（适用于 GitHub README.md）：

你现在复制下面这一整段就不会报错了👇

---

# 🧠 JD Cover Letter Generator Chrome Extension

This Chrome extension automatically extracts job descriptions from **LinkedIn**, **Seek**, and **Indeed**, then sends them to a Python backend (FastAPI + GPT) to generate tailored cover letters based on your resume.

## 🚀 Features

- ✅ Auto-detect job platforms: LinkedIn, Seek, Indeed  
- ✅ One-click resume editing in popup  
- ✅ Auto-fetch job description (JD) from current tab  
- ✅ Generates personalized cover letters using OpenAI GPT API

## 📦 Folder Structure

```
coverletter_plugin/
├── manifest.json
├── background.js
├── content.js
├── popup.html
```

## 🔌 Installation

1. Clone or download this repository.  
2. Open Chrome and go to `chrome://extensions/`  
3. Enable “Developer Mode”.  
4. Click **“Load unpacked”** and select the `coverletter_plugin/` folder.  
5. Pin the extension and open a job post on LinkedIn/Seek/Indeed.  
6. Click the extension icon and generate a cover letter!

## 💻 Backend Setup (FastAPI)

Backend repo (if split): [🔗 Backend code](./resume_coverletter_generator.py)

Make sure you have Python 3.8+ and install dependencies:

```bash
pip install fastapi uvicorn openai
```

Then run the backend:

```bash
uvicorn resume_coverletter_generator:app --reload
```

Set your OpenAI key via environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here   # macOS/Linux  
set OPENAI_API_KEY=your_api_key_here      # Windows CMD  
```

## ✍️ Resume Data Format (in plugin popup)

You can fill your resume details in the popup. Example:

```json
{
  "name": "Yixin (Charles) Zhang",
  "education": "Master of IT, UQ 2023",
  "experience": "6 months as software dev at current company",
  "skills": "Python, FastAPI, React Native",
  "projects": "Citrus YOLOv5, Impact-Portal, Playgrounds"
}
```

## 🛠️ Troubleshooting

- ❌ `uvicorn: command not found`  
  → Run `pip install uvicorn` and try again.

- ❌ JD not found  
  → Make sure you are on a valid job description page.

- ❌ CORS errors  
  → Ensure FastAPI backend has `CORSMiddleware` enabled.

## 📄 License

MIT License © 2025 Yixin Zhang (Charles Zhang)

---

如果你还需要我帮你生成 `LICENSE` 文件、或者一键部署 GitHub Pages 或部署文档，也可以继续说～
