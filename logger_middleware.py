# -*- coding: utf-8 -*-
"""
PMSA Cloud Logging & Score Analytics Middleware
Filename: logger_middleware.py
Description: Interoperability middleware for Webhook data push and student behavior logging.
"""

import datetime
import requests
import streamlit as st

WPS_WEBHOOK_URL = "https://www.kdocs.cn/chatflow/api/v2/func/webhook/3EspRZcftLE3c8SSMOu4VeBbqeO"
LOG_COLUMNS = [
    "Student_ID", "Chapter_Module", "Stage", "Action_Type",
    "User_Input_Cleaned", "Score_Total", "Score_Dim1", "Score_Dim2", "Score_Dim3", "Timestamp"
]

class PMSALoggerMiddleware:
    def __init__(self, url=WPS_WEBHOOK_URL):
        self.webhook_url = url

    def save_learning_log(self, student_id, chapter, stage, action, user_text, score_total, dim_scores=None):
        dim_scores = dim_scores or {}
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payload = {
            "Student_ID": str(student_id),
            "Chapter_Module": str(chapter),
            "Stage": str(stage),
            "Action_Type": str(action),
            "User_Input_Cleaned": str(user_text).replace(",", "，"),
            "Score_Total": float(round(score_total, 1)),
            "Score_Dim1": float(round(dim_scores.get("dim1", 0), 1)),
            "Score_Dim2": float(round(dim_scores.get("dim2", 0), 1)),
            "Score_Dim3": float(round(dim_scores.get("dim3", 0), 1)),
            "Timestamp": timestamp
        }

        if "cloud_logs_backup" in st.session_state:
            st.session_state.cloud_logs_backup.append(payload)

        if self.webhook_url:
            try:
                requests.post(self.webhook_url, json=payload, timeout=5)
            except Exception:
                pass

    def evaluate_mechanism_input(self, text, keywords):
        if not text:
            return 0.0, {"dim1": 0.0, "dim2": 0.0, "dim3": 0.0}
        
        matches = sum([1 for kw in keywords if kw.lower() in text.lower()])
        ratio = matches / max(1, len(keywords))
        score = min(100.0, 60.0 + ratio * 35.0 + min(5.0, len(text) / 20.0))
        
        return score, {
            "dim1": round(score * 0.95, 1),
            "dim2": round(score * 0.98, 1),
            "dim3": round(score * 1.02, 1)
        }