from langchain_core.language_models import BaseChatModel
from extraction_models import ProjectData
from extraction_prompt import EXTRACTION_PROMPT


class ProjectDataExtractor:
    """
    Class for extracting project data from text descriptions using LangChain and LLM with structured decoding.
    """

    def __init__(self, llm: BaseChatModel):
        """
        Initialize the extractor with LLM.

        Args:
            llm: LLM model - LLM must support structured decoding.
        """
        self.llm = llm
        self.structured_llm = self.llm.with_structured_output(ProjectData)

    def extract_data(self, text_description: str) -> ProjectData:
        """
        Extract project data from a text description using LangChain.

        Args:
            text_description: Text description of the project

        Returns:
            ProjectData object containing the extracted information

        Raises:
            ValueError: If there's an error in the extraction process
        """
        try:
            prompt = f"{EXTRACTION_PROMPT}\n\n{text_description}"

            project_data = self.structured_llm.invoke(prompt)
            return project_data

        except Exception:
            raise ValueError("Error during extraction")
