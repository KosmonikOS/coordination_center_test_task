from docxtpl import DocxTemplate
from formatted_data import FormattedProjectData


class ProjectPassportFiller:
    """
    Class for filling docx templates with extracted project data.
    """

    def __init__(self, template_path: str):
        """
        Initialize the filler with a template path.

        Args:
            template_path: Path to the .docx template file with placeholders
        """
        self.template = DocxTemplate(template_path)

    def fill_template(
        self, formatted_data: FormattedProjectData, output_path: str
    ) -> None:
        """
        Fill the template with project data and save to output path.

        Args:
            formatted_data: Formatted project data
            output_path: Path where to save the filled document
        """
        context = formatted_data.model_dump()
        self.template.render(context)
        self.template.save(output_path)
