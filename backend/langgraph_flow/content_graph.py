from typing import TypedDict
from typing import Optional

from langgraph.graph import StateGraph
from langgraph.graph import END

from services.content_service import (
    generate_chapter_content
)

# =========================================================
# STATE
# =========================================================

class ContentState(TypedDict):

    topic: str

    chapter_name: str

    model_name: str

    generated_content: Optional[str]

    final_content: Optional[str]

# =========================================================
# NODE 1
# GENERATE CONTENT
# =========================================================

def generate_content_node(state: ContentState):

    """
    Generate chapter content using LLM.
    """

    topic = state["topic"]

    chapter_name = state["chapter_name"]

    model_name = state["model_name"]

    content = generate_chapter_content(
        topic=topic,
        chapter_name=chapter_name,
        model_name=model_name
    )

    state["generated_content"] = content

    return state

# =========================================================
# NODE 2
# FINALIZE CONTENT
# =========================================================

def finalize_content_node(state: ContentState):

    """
    Final processing step.
    """

    generated_content = state.get(
        "generated_content",
        ""
    )

    state["final_content"] = generated_content

    return state

# =========================================================
# CREATE GRAPH
# =========================================================

def create_content_graph():

    """
    Create LangGraph workflow.
    """

    workflow = StateGraph(ContentState)

    # -----------------------------------------------------
    # ADD NODES
    # -----------------------------------------------------

    workflow.add_node(
        "generate_content",
        generate_content_node
    )

    workflow.add_node(
        "finalize_content",
        finalize_content_node
    )

    # -----------------------------------------------------
    # ENTRY POINT
    # -----------------------------------------------------

    workflow.set_entry_point(
        "generate_content"
    )

    # -----------------------------------------------------
    # EDGES
    # -----------------------------------------------------

    workflow.add_edge(
        "generate_content",
        "finalize_content"
    )

    workflow.add_edge(
        "finalize_content",
        END
    )

    # -----------------------------------------------------
    # COMPILE
    # -----------------------------------------------------

    graph = workflow.compile()

    return graph
