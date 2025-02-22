from datetime import date
from pydantic import BaseModel
from extraction_models import ProjectData


class FormattedProjectData(BaseModel):
    """
    Formatted project data ready for template rendering.
    """

    project_name: str
    project_start_order_form: str
    project_goal: str
    project_result_vision: str
    project_constraints_exclusions: str
    project_risks_assumptions: str
    project_stakeholders: str
    project_steering_committee: str
    project_start_date: str
    project_end_date: str
    project_stages_results: str
    project_initiator: str
    project_owner: str
    project_owner_representative: str
    project_leader: str
    management_team_curator: str
    project_manager: str
    strategy_portfolio_leader: str
    strategy_event_leader: str
    independent_experts: list[str]

    def model_dump(self) -> dict:
        """Override model_dump to include computed properties."""
        base_dict = super().model_dump()
        base_dict["project_team"] = self.project_team
        return base_dict

    @classmethod
    def from_project_data(cls, project_data: ProjectData) -> "FormattedProjectData":
        """Create formatted data from ProjectData."""

        def format_date(date_obj: date) -> str:
            """Format date to Russian format."""
            return date_obj.strftime("%d.%m.%Y") if date_obj else ""

        def format_stages_results(stages: list) -> str:
            """Format project stages and results."""
            result = []
            for i, stage in enumerate(stages, 1):
                stage_results = "\n".join(
                    [f"• {result}" for result in stage.smart_results]
                )
                stage_text = (
                    f"Этап №{i}\n"
                    f"{format_date(stage.stage_start_date)}-{format_date(stage.stage_end_date)}.\n"
                    f"{stage.stage_name}:\n"
                    f"{stage_results}"
                )
                result.append(stage_text)
            return "\n\n".join(result)

        def format_end_date(stages: list) -> str:
            """Format project end dates based on stages."""
            result = []
            for i, stage in enumerate(stages, 1):
                result.append(f"Этап {i} – {format_date(stage.stage_end_date)}")
            return "\n".join(result)

        team = project_data.project_team
        return cls(
            project_name=project_data.project_name,
            project_start_order_form=project_data.project_start_order_form,
            project_goal=project_data.project_goal,
            project_result_vision=project_data.project_result_vision,
            project_constraints_exclusions="\n".join(
                project_data.project_constraints_exclusions
            ),
            project_risks_assumptions="\n".join(project_data.project_risks_assumptions),
            project_stakeholders="\n".join(project_data.project_stakeholders),
            project_steering_committee="\n".join(
                project_data.project_steering_committee
            ),
            project_start_date=format_date(project_data.project_start_date),
            project_end_date=format_end_date(project_data.project_stages),
            project_stages_results=format_stages_results(project_data.project_stages),
            project_initiator=team.project_initiator or "Не указан",
            project_owner=team.project_owner or "Не указан",
            project_owner_representative=team.project_owner_representative
            or "Не указан",
            project_leader=team.project_leader or "Не указан",
            management_team_curator=team.management_team_curator or "Не указан",
            project_manager=team.project_manager or "Не указан",
            strategy_portfolio_leader=team.strategy_portfolio_leader or "Не указан",
            strategy_event_leader=team.strategy_event_leader or "Не указан",
            independent_experts=team.independent_experts
            if team.independent_experts
            else [],
        )

    @property
    def project_team(self) -> str:
        """Format project team into a string for template rendering."""

        def format_team_member(title: str, fullname: str) -> str:
            return f"{title}: {fullname}"

        team_formatted = [
            format_team_member("Инициатор проекта", self.project_initiator),
            format_team_member("Владелец проекта", self.project_owner),
            format_team_member(
                "Представитель Владельца проекта", self.project_owner_representative
            ),
            format_team_member("Руководитель проекта", self.project_leader),
            format_team_member(
                "Куратор команды управления", self.management_team_curator
            ),
            format_team_member("Менеджер проекта", self.project_manager),
            format_team_member(
                "Руководитель портфеля мероприятий Стратегии",
                self.strategy_portfolio_leader,
            ),
            format_team_member(
                "Руководитель мероприятия Стратегии", self.strategy_event_leader
            ),
        ]

        if self.independent_experts:
            for expert in self.independent_experts:
                team_formatted.append(
                    format_team_member("Независимый эксперт", f"{expert}")
                )

        return "\n".join(team_formatted)
