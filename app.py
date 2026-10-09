# -*- coding: utf-8 -*-
"""
PMSA-FoodBiochem AI Workstation Main Entry
Filename: app.py
Description: Main UI and controller script.
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from config_translations import TRANSLATIONS, MODULE_DESCRIPTIONS
from data_engine import BioChemDataEngine, CASE_DATA_ENGINE
from logger_middleware import PMSALoggerMiddleware, LOG_COLUMNS

st.set_page_config(
    page_title="PMSA-FoodBiochem Workstation V2.0",
    layout="wide",
    page_icon="🔬"
)

# 初始化系统服务
engine = BioChemDataEngine()
logger = PMSALoggerMiddleware()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Helvetica+Neue:wght=300;400;600&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #F8FAFC;
    }
    .pmsa-card { padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border-left: 6px solid; }
    .card-problem { background-color: #EBF8FF; border-left-color: #3182CE; }
    .card-mechanism { background-color: #E6FFFA; border-left-color: #319795; }
    .card-simulation { background-color: #F0FFF4; border-left-color: #38A169; }
    .card-application { background-color: #F7FAFC; border-left-color: #2F855A; }
    .card-analytics { background-color: #FFFAF0; border-left-color: #DD6B20; }
    .main-title { color: #1A365D; font-weight: 700; font-size: 2.4rem; text-align: center; margin-bottom: 5px; }
    .sub-title { color: #4A5568; font-size: 1.1rem; text-align: center; margin-bottom: 25px; font-style: italic; }
</style>
""", unsafe_allow_html=True)

if "user_role" not in st.session_state: st.session_state.user_role = None
if "uid" not in st.session_state: st.session_state.uid = ""
if "cloud_logs_backup" not in st.session_state: st.session_state.cloud_logs_backup = []

# 登录逻辑
if st.session_state.user_role is None:
    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
    _, c2, _ = st.columns([1, 1.8, 1])
    with c2:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center; color: #1A365D;'>🔬 PMSA-FoodBiochem AI 智慧工作站 V2.0</h3>", unsafe_allow_html=True)
            st.write("---")
            input_uid = st.text_input("👤 请输入学号/工号 (ID):")
            access_token = st.text_input("🔑 请输入系统密钥 (Access Token):", type="password")

            if st.button("激活并进入工作站", type="primary", use_container_width=True):
                if not input_uid:
                    st.error("❌ 请输入凭证。")
                elif access_token == "student2026":
                    st.session_state.user_role = "Student"
                    st.session_state.uid = input_uid
                    st.rerun()
                elif access_token == "teacher7788":
                    st.session_state.user_role = "Teacher"
                    st.session_state.uid = f"Instructor_{input_uid}"
                    st.rerun()
                else:
                    st.error("❌ 访问密钥无效。")
else:
    lang = st.sidebar.selectbox(TRANSLATIONS["zh"]["lang_label"], ["zh", "en"])
    t_t = TRANSLATIONS[lang]

    st.sidebar.markdown(f"<div style='background-color:#EDF2F7; padding:12px; border-radius:8px; margin-bottom:15px;'><p style='margin-bottom:4px; font-size:13px;'>👤 <b>ID:</b> <code style='color:#2B6CB0;'>{st.session_state.uid}</code></p><p style='margin-bottom:0px; font-size:13px;'>🎖️ <b>Role:</b> <code style='color:#2F855A;'>{st.session_state.user_role}</code></p></div>", unsafe_allow_html=True)

    if st.sidebar.button(t_t["logout_btn"], use_container_width=True):
        st.session_state.user_role = None
        st.session_state.uid = ""
        st.rerun()

    st.sidebar.markdown("---")
    case_idx = st.sidebar.selectbox(t_t["lbl_case"], range(len(t_t["cases"])), format_func=lambda x: t_t["cases"][x])
    step_name = st.sidebar.radio(t_t["lbl_step"], t_t["steps"])

    st.markdown(f"<h1 class='main-title'>{t_t['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='sub-title'>{t_t['sub']}</p>", unsafe_allow_html=True)

    module_info = MODULE_DESCRIPTIONS[case_idx][lang]
    df_sim = engine.get_dataset(case_idx)

    # 1. Problem 环节
    if "Problem" in step_name or "科学情境" in step_name:
        st.markdown(f"<div class='pmsa-card card-problem'><h3>{t_t['p_bg']}</h3></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            with st.container(border=True):
                st.markdown(f"#### {t_t['p_bg']}")
                st.info(module_info["problem"])
        with c2:
            with st.container(border=True):
                st.markdown(f"#### {t_t['p_focus']}")
                st.success(module_info["mechanism"])
        st.markdown("---")
        st.markdown(f"### {t_t['p_task']}")
        c_t1, c_t2 = st.columns([2, 1])
        with c_t1:
            st.markdown(t_t["p_task_1"])
            st.markdown(f"💡 **Application Target:** `{module_info['application']}`")
        with c_t2:
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label=t_t["p_download_btn"],
                data=df_sim.to_csv(index=False).encode("utf-8-sig"),
                file_name=f"FoodBiochem_Template_Module_{case_idx + 1}.csv",
                mime="text/csv",
                use_container_width=True
            )

    # 2. Mechanism 环节
    elif "Mechanism" in step_name or "机制建构" in step_name:
        st.markdown(f"<div class='pmsa-card card-mechanism'><h3>🌿 {t_t['m_title']}</h3></div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1.2, 1])
        with c1:
            st.write(f"**{t_t['m_keyword_lbl']}**")
            kws = CASE_DATA_ENGINE[case_idx]["kws"]
            st.code(", ".join(kws))
            u_map = st.text_area(t_t["m_lbl"], placeholder=t_t["m_holder"], height=180)
            submit_m = st.button(t_t["m_btn"], type="primary", use_container_width=True)
        with c2:
            if submit_m and u_map:
                score, dims = logger.evaluate_mechanism_input(u_map, kws)
                logger.save_learning_log(st.session_state.uid, t_t["cases"][case_idx], "Mechanism", "Submit_Map", u_map, score, dims)
                st.markdown("#### 🤖 AI Feedback Dashboard")
                st.success(t_t["m_success"])

    # 3. Simulation 环节
    elif "Simulation" in step_name or "数据分析" in step_name:
        st.markdown(f"<div class='pmsa-card card-simulation'><h3>📊 {t_t['s_title']}</h3></div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1.5])
        with c1:
            upl = st.file_uploader(t_t["s_upload"], type=["csv", "xlsx"])
            df_use = df_sim.copy()
            st.markdown(f"##### {t_t['s_preview']}")
            st.dataframe(df_use, height=260, use_container_width=True)
        with c2:
            fig, ax = plt.subplots(figsize=(6, 3.5), dpi=150)
            x_col = CASE_DATA_ENGINE[case_idx]["x"]
            y_cols = [c for c in df_use.columns if c != x_col]
            for col in y_cols:
                ax.plot(df_use[x_col], df_use[col], marker="o", lw=2, label=col)
            ax.set_xlabel(x_col)
            ax.set_title(f"Biochemical Kinetics Trend (Module {case_idx + 1})")
            ax.legend()
            ax.grid(True, linestyle="--", alpha=0.5)
            fig.tight_layout()
            st.pyplot(fig)
            plt.close()

    # 4. Application 环节
    elif "Application" in step_name or "方案应用" in step_name:
        st.markdown(f"<div class='pmsa-card card-application'><h3>🚀 {t_t['a_title']}</h3></div>", unsafe_allow_html=True)
        st.markdown(f"{t_t['a_task_lbl']} <code style='color:#2F855A; font-size:14px;'>{module_info['application']}</code>", unsafe_allow_html=True)
        st.write(t_t["a_intro"])

        with st.form("app_form_v2_0"):
            st.markdown(f"#### {t_t['a_part1']}")
            c1, c2 = st.columns([2, 1])
            with c1:
                t_in = st.text_input(t_t["a_p1_name"], placeholder=t_t["a_p1_name_holder"])
            with c2:
                tech_route = st.selectbox(t_t["a_p1_route"], t_t["a_routes"])

            st.markdown(f"#### {t_t['a_part2']}")
            st.markdown(f"**{t_t['a_t1_lbl']}**")
            st.caption(t_t["a_t1_cap"])
            formula_design = st.text_area("Input 1:", placeholder=t_t["a_t1_holder"], height=90, label_visibility="collapsed")

            st.markdown(f"**{t_t['a_t2_lbl']}**")
            st.caption(t_t["a_t2_cap"])
            mechanism_explain = st.text_area("Input 2:", placeholder=t_t["a_t2_holder"], height=90, label_visibility="collapsed")

            st.markdown(f"**{t_t['a_t3_lbl']}**")
            st.caption(t_t["a_t3_cap"])
            evaluation_plan = st.text_area("Input 3:", placeholder=t_t["a_t3_holder"], height=90, label_visibility="collapsed")

            st.markdown(f"#### {t_t['a_part3']}")
            upl_file = st.file_uploader(t_t["a_file_lbl"], type=["pdf", "docx", "xlsx", "png"])

            if st.form_submit_button(t_t["a_submit_btn"], type="primary", use_container_width=True):
                if not t_in or not formula_design or not mechanism_explain or not evaluation_plan:
                    st.error("❌ 填写不完整 / Incomplete Form")
                else:
                    full_submission_text = (
                        f"【方案名称】: {t_in}\n"
                        f"【生物技术路径】: {tech_route}\n"
                        f"【任务1-生化工艺参数】: {formula_design}\n"
                        f"【任务2-生化与代谢机制】: {mechanism_explain}\n"
                        f"【任务3-生化指标验证】: {evaluation_plan}"
                    )
                    char_count = len(formula_design) + len(mechanism_explain) + len(evaluation_plan)
                    score = min(100.0, 72.0 + (char_count / 15.0))

                    logger.save_learning_log(
                        st.session_state.uid,
                        t_t["cases"][case_idx],
                        "Application",
                        "Submit_Scheme",
                        full_submission_text,
                        score,
                        {"dim1": score * 0.96, "dim2": score, "dim3": score * 1.01}
                    )
                    st.success(t_t["a_success"])
                    st.balloons()

    # 5. Analytics 环节
    elif "Analytics" in step_name or "智能评价" in step_name:
        an_title_text = t_t.get("an_title", "智能评价分析")
        st.markdown(f"<div class='pmsa-card card-analytics'><h3>📈 {an_title_text}</h3></div>", unsafe_allow_html=True)

        df_logs = pd.DataFrame(st.session_state.cloud_logs_backup, columns=LOG_COLUMNS)
        if df_logs.empty:
            st.warning(t_t.get("an_no_data"))
        else:
            st.markdown(f"### 👤 {t_t.get('an_user_logs')} (ID: {st.session_state.uid})")
            st.dataframe(df_logs, use_container_width=True)