import streamlit as st
from google import genai
from pathlib import Path
from datetime import datetime

status = "read"

if status == "generate":
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    with open("Reading Material.txt", "r", encoding="utf-8") as f:
        text = f.read()

    prompt = f"""
    You are an experienced teacher creating revision notes for students preparing for an exam.

    Your goal is NOT to shorten the text.
    Your goal is to identify and explain ONLY the information that is most important to remember.

    # Rules

    Return ONLY valid Markdown.
    Do NOT wrap the response inside code fences.

    Imagine the student has only 20 minutes before the exam.
    Include only the concepts that are actually worth memorizing.

    Skip:
    - Long explanations.
    - Repeated ideas.
    - Multiple examples of the same concept.
    - Stories.
    - Historical background.
    - Real-world incidents unless they teach an important lesson.
    - Large lists where only a few items matter.

    Keep:
    - Definitions.
    - Main concepts.
    - Core principles.
    - Important differences between concepts.
    - Key security practices.
    - Anything that introduces a new idea.
    - Information likely to appear in an exam.

    # How to summarize

    For each topic:

    - Start with a short overview (1–2 sentences).
    - Explain only the essential concepts.
    - If there are many examples, keep only ONE simple example.
    - If there are many methods or lists, mention only the most important ones.
    - Merge repeated information.
    - Do not repeat definitions from previous topics.

    If a section contains many details, ask yourself:

    "Would forgetting this hurt the student's understanding?"

    If the answer is **No**, leave it out.

    # Markdown Style

    Use Markdown to make the notes enjoyable to read.

    Use:

    # Main title

    ## Topic

    ### Concept

    - Bullet points
    - Numbered lists when appropriate

    Use tables ONLY when comparing concepts.

    Use emojis naturally to make sections easy to scan.

    Examples:

    ## 🔐 CIA Triad

    ### 🔒 Confidentiality

    instead of

    ## CIA Triad

    Use these kinds of emojis:
    📌 🔐 🔑 🛡️ 🌐 💡 ⚠️ ✅ 📖 🎯

    Highlight important terms using **bold**.

    Use blockquotes only for important exam tips.

    Use horizontal rules between major topics.

    Keep paragraphs short.

    # Streamlit Colors

    The final output will be displayed using **Streamlit's Markdown renderer**, which supports colored text using the following syntax:

    :color[text]

    Use this syntax whenever it improves readability.

    Available colors include:

    - :red[text]
    - :orange[text]
    - :yellow[text]
    - :green[text]
    - :blue[text]
    - :violet[text]
    - :gray[text]
    - :rainbow[text]

    Examples:

    ## :blue[🌐 Digital Transformation]

    ### :green[Definition]

    **:orange[Important:]** Technology changes how people and organizations perform tasks.

    > :red[Exam Tip:] Remember the definition rather than the examples.

    Use colors consistently throughout the document.

    Recommended usage:

    - **Blue** → Main topics and section titles.
    - **Green** → Definitions and key concepts.
    - **Orange** → Important notes and reminders.
    - **Red** → Warnings, risks, security threats, or common mistakes.
    - **Yellow** → Examples.
    - **Violet** → Comparisons or special concepts.
    - **Rainbow** → Document title only (sparingly).
    - **Gray** → Minor notes or additional information.

    Do NOT overuse colors.
    Use them only to improve readability and visual organization.

    # Length

    Target about **20-30% of the original material.**

    Prefer understanding over completeness.

    A student should be able to read these notes quickly and still answer most exam questions.

    # Style

    Formal.
    Clear.
    Easy to revise.
    Easy to scan.
    Professional.

    DO NOT exceed 5000 words.

    Return ONLY the Markdown document.

    Learning Material:

    ```text
    {text}
    ```
    """

    with st.spinner("Generating..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

    result = response.text

    # Create results folder if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    output_file = results_dir / f"summary_{timestamp}.md"

    # Save Markdown output
    output_file.write_text(result, encoding="utf-8")

    st.markdown(result)

elif status == "read":
    st.markdown("# :rainbow[Cybersecurity & Digital Arts Revision Notes]")


    tab1, tab2, tab3, tab4 = st.tabs(["🛡️ Week 11", "👾 Week 12", "⚔️ Week 13", "🎨 Week 14"])

    with tab1:
        file_path = "results/final_summary_w11.md"

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        
        st.markdown(md)
    
    with tab2:
        file_path = "results/final_summary_w12.md"

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        
        st.markdown(md)
    
    with tab3:
        file_path = "results/final_summary_w13.md"

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        
        st.markdown(md)
    
    with tab4:
        file_path = "results/final_summary_w14.md"

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()
        
        st.markdown(md)