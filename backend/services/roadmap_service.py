from services.llm_service import get_llm
import json

def generate_roadmap(topic, model_name):

    llm = get_llm(model_name)

    prompt = f"""
You are an expert educational curriculum designer.

Create a COMPLETE professional learning roadmap.

TOPIC:
{topic}

IMPORTANT:

Generate ONLY VALID JSON.

DO NOT write explanations.
DO NOT use markdown.
DO NOT use ```json.


OTHER IMPORTANT INSTRUCTIONS:

1. Create roadmap in STRICT chapter-wise format
2. Start from beginner level
3. Gradually move to advanced level
4. Each chapter must contain:
    - Chapter title
    - Numbered subtopics
5. Keep roadmap practical and industry oriented
6. Include real-world concepts
7. DO NOT generate explanations
8. DO NOT generate content paragraphs
9. ONLY generate roadmap structure
10. DO NOT include any unwanted external topic not related to the main topic
11. DO NOT SKIP any important topic related to the main topic

OUTPUT FORMAT MUST BE EXACTLY LIKE THIS:

{{
    "topic": "{topic}",
    "chapters": [
        {{
            "chapter_title": "Chapter 1: Introduction",
            "subtopics": [
                "What is Python",
                "Features of Python"
            ]
        }}
    ]
}}


Generate at least:
- 5 to 10 chapters
- Each chapter should contain 5 to 8 most important subtopics

IMPORTANT:
Do NOT break the structure.
Follow the format strictly.
"""

    response = llm.invoke(prompt)

    content = response.content

    # Remove markdown if model adds it

    content = content.replace(
        "```json",
        ""
    )

    content = content.replace(
        "```",
        ""
    )

    roadmap_json = json.loads(content)

    return roadmap_json
