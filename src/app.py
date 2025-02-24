from settings import settings
from extractor import ProjectDataExtractor
from docx_filler import ProjectPassportFiller
from formatted_data import FormattedProjectData
from langchain_groq import ChatGroq
from logger import setup_logging
import streamlit as st
import os
import tempfile
import logging


def init_llm():
    """Initialize LLM model."""
    return ChatGroq(
        api_key=settings.openai_api_key,
        model_name=settings.openai_model,
        temperature=settings.openai_temperature,
    )


def main():
    setup_logging()
    st.title("Генератор паспорта проекта")

    if "formatted_data" not in st.session_state:
        st.session_state.formatted_data = None

    # Text input for project description
    text_description = st.text_area(
        "Описание проекта",
        height=300,
        help="Введите описание проекта для генерации паспорта",
    )

    # Process button
    if st.button("Обработать"):
        with st.spinner("Обрабатываем описание проекта..."):
            try:
                # Initialize extractor and process description
                llm = init_llm()
                extractor = ProjectDataExtractor(llm)
                project_data = extractor.extract_data(text_description)

                # Format extracted data
                st.session_state.formatted_data = (
                    FormattedProjectData.from_project_data(project_data)
                )
                st.success("Данные успешно извлечены!")
            except Exception as e:
                logging.error(f"Error processing description: {str(e)}", exc_info=True)
                st.error(f"Ошибка при обработке")
                return

    # Show editable fields if data is extracted
    if st.session_state.formatted_data:
        st.subheader("Проверьте и отредактируйте данные")

        formatted_data = st.session_state.formatted_data

        any_empty_field = False

        formatted_data.project_name = st.text_input(
            "Название проекта *",
            formatted_data.project_name,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_name:
            any_empty_field = True

        formatted_data.project_start_order_form = st.text_input(
            "Поручение о старте проекта *",
            formatted_data.project_start_order_form,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_start_order_form:
            any_empty_field = True

        formatted_data.project_goal = st.text_area(
            "Цель проекта *",
            formatted_data.project_goal,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_goal:
            any_empty_field = True

        formatted_data.project_result_vision = st.text_area(
            "Образ результата *",
            formatted_data.project_result_vision,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_result_vision:
            any_empty_field = True

        formatted_data.project_constraints_exclusions = st.text_area(
            "Ограничения и исключения (каждое с новой строки) *",
            formatted_data.project_constraints_exclusions,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_constraints_exclusions:
            any_empty_field = True

        formatted_data.project_risks_assumptions = st.text_area(
            "Риски и допущения (каждое с новой строки) *",
            formatted_data.project_risks_assumptions,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_risks_assumptions:
            any_empty_field = True

        formatted_data.project_stakeholders = st.text_area(
            "Заинтересованные стороны (каждая с новой строки) *",
            formatted_data.project_stakeholders,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_stakeholders:
            any_empty_field = True

        formatted_data.project_start_date = st.text_input(
            "Дата начала проекта *",
            formatted_data.project_start_date,
            placeholder="ДД.ММ.ГГГГ",
        )
        if not formatted_data.project_start_date:
            any_empty_field = True

        formatted_data.project_end_date = st.text_area(
            "Даты окончания этапов *",
            formatted_data.project_end_date,
            height=100,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_end_date:
            any_empty_field = True

        formatted_data.project_stages_results = st.text_area(
            "Этапы и результаты *",
            formatted_data.project_stages_results,
            height=200,
            placeholder="Обязательное поле",
        )
        if not formatted_data.project_stages_results:
            any_empty_field = True

        with st.expander("Команда проекта"):
            formatted_data.project_initiator = st.text_input(
                "Инициатор проекта *",
                formatted_data.project_initiator,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_initiator:
                any_empty_field = True

            formatted_data.project_owner = st.text_input(
                "Владелец проекта *",
                formatted_data.project_owner,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_owner:
                any_empty_field = True

            formatted_data.project_owner_representative = st.text_input(
                "Представитель владельца проекта *",
                formatted_data.project_owner_representative,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_owner_representative:
                any_empty_field = True

            formatted_data.project_leader = st.text_input(
                "Руководитель проекта *",
                formatted_data.project_leader,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_leader:
                any_empty_field = True

            formatted_data.management_team_curator = st.text_input(
                "Куратор команды управления *",
                formatted_data.management_team_curator,
                placeholder="Обязательное поле",
            )
            if not formatted_data.management_team_curator:
                any_empty_field = True

            formatted_data.project_manager = st.text_input(
                "Менеджер проекта *",
                formatted_data.project_manager,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_manager:
                any_empty_field = True

            formatted_data.strategy_portfolio_leader = st.text_input(
                "Руководитель портфеля мероприятий Стратегии *",
                formatted_data.strategy_portfolio_leader,
                placeholder="Обязательное поле",
            )
            if not formatted_data.strategy_portfolio_leader:
                any_empty_field = True

            formatted_data.strategy_event_leader = st.text_input(
                "Руководитель мероприятия Стратегии *",
                formatted_data.strategy_event_leader,
                placeholder="Обязательное поле",
            )
            if not formatted_data.strategy_event_leader:
                any_empty_field = True

            experts_text = st.text_area(
                "Независимые эксперты (каждый с новой строки)",
                "\n".join(formatted_data.independent_experts),
                height=100,
                placeholder="Необязательное поле",
            )
            formatted_data.independent_experts = [
                e.strip() for e in experts_text.split("\n") if e.strip()
            ]

            formatted_data.project_steering_committee = st.text_area(
                "Состав УКП (каждый с новой строки) *",
                formatted_data.project_steering_committee,
                height=100,
                placeholder="Обязательное поле",
            )
            if not formatted_data.project_steering_committee:
                any_empty_field = True

        # Generate document button
        if st.button("Сгенерировать документ"):
            if any_empty_field:
                st.error(
                    "Пожалуйста, заполните все обязательные поля перед генерацией документа"
                )
                return

            with st.spinner("Генерируем паспорт проекта..."):
                try:
                    # Create temporary file for template
                    with tempfile.NamedTemporaryFile(
                        suffix=".docx", delete=False
                    ) as tmp_file:
                        # Initialize filler with template
                        filler = ProjectPassportFiller(settings.template_path)

                        # Fill template and save
                        filler.fill_template(formatted_data, tmp_file.name)

                        # Provide download button
                        with open(tmp_file.name, "rb") as file:
                            st.download_button(
                                label="Скачать паспорт проекта",
                                data=file,
                                file_name="project_passport.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            )
                        os.remove(tmp_file.name)
                except Exception as e:
                    logging.error(f"Error generating document: {str(e)}", exc_info=True)
                    st.error(f"Ошибка при генерации документа")


if __name__ == "__main__":
    main()
