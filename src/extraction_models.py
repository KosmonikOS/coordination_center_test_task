from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class ProjectStage(BaseModel):
    """
    Model for each stage of the project.
    Will be used to extract data via LLM structured decoding.
    """

    stage_name: str = Field(
        ...,
        description="Название этапа",
        examples=[
            "Сбор данных у граждан",
            "Анализ и выявление острых проблем",
            "Реализация пилотного проекта",
            "Тестирование в малых регионах",
        ],
    )
    stage_start_date: date = Field(
        ...,
        description="Дата начала этапа (формат YYYY-MM-DD)",
        example="2023-01-01",
    )
    stage_end_date: date = Field(
        ...,
        description="Дата окончания этапа (формат YYYY-MM-DD)",
        example="2023-12-31",
    )
    smart_results: list[str] = Field(
        ..., description="Результаты, прописанные по методологии SMART"
    )


class ProjectTeam(BaseModel):
    """
    Model for the project team roles and members.
    Will be used to extract data via LLM structured decoding.
    """

    project_initiator: Optional[str] = Field(
        None,
        description="Инициатор проекта: Принимает решение о необходимости реализации проекта, определяет высокоуровневые требования и назначает владельца проекта.",
        example="Д.Н. Иванов",
    )
    project_owner: Optional[str] = Field(
        None,
        description="Владелец проекта: Даёт поручения о запуске проекта, утверждает паспорт проекта, назначает руководителя проекта и куратора команды управления.",
        example="Д.Н. Иванов",
    )
    project_management_committee: Optional[str] = Field(
        None,
        description="Управляющий комитет проекта: Согласовывает паспорт проекта и изменения, определяет цели и контролирует реализацию этапов.",
        example="Д.Н. Иванов",
    )
    project_owner_representative: Optional[str] = Field(
        None,
        description="Представитель Владельца проекта: Обеспечивает проведение совещаний и коммуникацию между сторонами.",
        example="Д.Н. Иванов",
    )
    project_leader: Optional[str] = Field(
        None,
        description="Руководитель проекта (РП): Формирует паспорт проекта, управляет командой и обеспечивает эскалацию рисков.",
        example="Д.Н. Иванов",
    )
    management_team_curator: Optional[str] = Field(
        None,
        description="Куратор команды управления: Предоставляет информацию об оценке необходимых ресурсов и формирует предложения по команде.",
        example="Д.Н. Иванов",
    )
    project_manager: Optional[str] = Field(
        None,
        description="Менеджер проекта (МП): Координирует реализацию плана проекта, отвечает за организацию мероприятий и ведение отчетности.",
        example="Д.Н. Иванов",
    )
    strategy_portfolio_leader: Optional[str] = Field(
        None,
        description="Руководитель портфеля мероприятий Стратегии: Формирует сводную оценку и согласовывает цели и планы мероприятий.",
        example="Д.Н. Иванов",
    )
    strategy_event_leader: Optional[str] = Field(
        None,
        description="Руководитель мероприятия Стратегии: Формирует детализированный план реализации мероприятия и управляет его выполнением.",
        example="Д.Н. Иванов",
    )
    independent_experts: Optional[list[str]] = Field(
        None,
        description="Независимые эксперты проекта: Оценивают эффективность реализации мероприятий и проводят аудит проекта.",
        example=["Д.Н. Иванов", "А.С. Петров"],
    )


class ProjectData(BaseModel):
    """
    Main model that holds all the fields to extract from the LLM's JSON output.
    Will be used to extract data via LLM structured decoding.
    """

    project_name: str = Field(
        ..., description="Наименование проекта", example="Обработка обращений граждан"
    )
    project_start_order_form: str = Field(
        ...,
        description="Поручение о старте проекта (форма поручения, устное/письменное поручение)",
        example="Письменное поручение",
    )
    project_goal: str = Field(
        ...,
        description="Цель проекта: краткое описание ключевых задач и результатов, которых проект стремится достичь.",
        example="Повысить оперативность реагирования на обращения граждан.",
    )
    project_result_vision: str = Field(
        ...,
        description="Образ результата проекта: описание итогового результата и его характеристик, демонстрирующих успех проекта.",
        example="Интерактивная платформа с быстрым доступом к аналитическим данным.",
    )
    project_stages: list[ProjectStage] = Field(
        ..., description="Список этапов и результатов проекта"
    )
    project_constraints_exclusions: list[str] = Field(
        ...,
        description="Ограничения и исключения проекта: список ограничений, рамок и аспектов, которые вне сферы проекта, влияющих на его реализацию.",
        example=["Финансовые ограничения", "Ограниченный кадровый состав"],
    )
    project_risks_assumptions: list[str] = Field(
        ...,
        description="Риски и допущения проекта: перечень потенциальных угроз и предположений, на которых базируется план реализации проекта.",
        example=["Риск задержки поставок", "Предположение о стабильности рынка"],
    )
    project_stakeholders: list[str] = Field(
        ...,
        description="Список заинтересованных сторон: основные группы и/или физические лица, которые имеют интересы в реализации проекта или могут на него влиять.",
        example=[
            "Министерство здравоохранения Российской Федерации",
            "Федеральная служба по надзору в сфере энергетики",
        ],
    )
    project_steering_committee: list[str] = Field(
        ...,
        description="Состав Управляющего комитета проекта: список членов комитета, ответственных за стратегический контроль и ключевые решения по проекту.",
        example=["Шубин", "Ицхаков", "Белова"],
    )
    project_team: ProjectTeam = Field(..., description="Команда проекта")
    project_start_date: date = Field(
        ...,
        description="Дата начала проекта (формат YYYY-MM-DD)",
        example="2023-01-01",
    )