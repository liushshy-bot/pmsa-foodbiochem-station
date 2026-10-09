# -*- coding: utf-8 -*-
"""
PMSA-FoodBiochem Simulation & Calculation Engine Module
Filename: data_engine.py
Description: Mathematical calculation engines for Michaelis-Menten kinetics, proteolysis, lipid oxidation, and flavor biogenesis.
"""

import numpy as np
import pandas as pd

class BioChemDataEngine:
    def __init__(self, seed=42):
        np.random.seed(seed)

    def generate_ppo_kinetics(self):
        """1. 酶促反应与动力学调控 (PPO 米氏方程与竞争性抑制)"""
        substrates = [0.5, 1.0, 2.0, 4.0, 8.0, 12.0]
        v_control = [round(15.0 * s / (2.0 + s) + np.random.normal(0, 0.2), 2) for s in substrates]
        v_inhibitor = [round(15.0 * s / (5.0 + s) + np.random.normal(0, 0.2), 2) for s in substrates]
        return pd.DataFrame({
            "Substrate_mM": substrates,
            "V_Control_(uM/min)": v_control,
            "V_Inhibitor_(uM/min)": v_inhibitor
        })

    def generate_meat_aging(self):
        """2. 内源酶与肌肉食品采后成熟 (Calpain 酶解 Desmin 与剪切力降解)"""
        days = [0, 1, 3, 5, 7, 14]
        desmin = [round(100.0 * np.exp(-0.25 * d) + np.random.normal(0, 1.5), 1) for d in days]
        shear_force = [round(8.5 * np.exp(-0.18 * d) + 2.5 + np.random.normal(0, 0.2), 2) for d in days]
        return pd.DataFrame({
            "Aging_Days": days,
            "Desmin_Intact_(%)": desmin,
            "WBSF_Shear_Force_(kg)": shear_force
        })

    def generate_maillard(self):
        """3. 糖类代谢途径与美拉德变化 (天冬酰胺酶预处理阻断丙烯酰胺)"""
        temp_c = [120, 140, 160, 180, 200]
        acrylamide_ctrl = [round(15.0 * np.exp(0.025 * (t - 120)) + np.random.normal(0, 2.0), 1) for t in temp_c]
        acrylamide_enz = [round(a * 0.15 + np.random.normal(0, 0.5), 1) for a in acrylamide_ctrl]
        return pd.DataFrame({
            "Temperature_(C)": temp_c,
            "Acrylamide_Control_(ug/kg)": acrylamide_ctrl,
            "Acrylamide_Asparaginase_(ug/kg)": acrylamide_enz
        })

    def generate_lipid_oxidation(self):
        """4. 脂质自由基过氧化与酶促氧化 (POV 与 MDA 积累)"""
        days = [0, 5, 10, 15, 20, 30]
        pov = [round(0.5 + 0.8 * d + np.random.normal(0, 0.3), 2) for d in days]
        mda = [round(0.05 + 0.04 * d + np.random.normal(0, 0.01), 3) for d in days]
        return pd.DataFrame({
            "Storage_Days": days,
            "POV_(meq/kg)": pov,
            "MDA_Content_(mg/kg)": mda
        })

    def generate_fermentation(self):
        """5. 食品发酵微生态与代谢生物转化 (LAB 发酵产酸与 pH 动力学)"""
        hours = [0, 2, 4, 6, 8, 12, 24]
        ph = [round(6.6 - 2.2 / (1.0 + np.exp(-0.4 * (h - 5))) + np.random.normal(0, 0.05), 2) for h in hours]
        lactic_acid = [round(0.1 + 0.8 / (1.0 + np.exp(-0.4 * (h - 5))) + np.random.normal(0, 0.02), 2) for h in hours]
        return pd.DataFrame({
            "Fermentation_Hours": hours,
            "pH_Value": ph,
            "Lactic_Acid_(%)": lactic_acid
        })

    def generate_flavor(self):
        """6. 风味前体物的生物合成与转化 (LOX/ADH 前体生成与挥发性酯类)"""
        days = [0, 2, 4, 6, 8, 10]
        hexanal = [round(120.0 * np.exp(-0.2 * d) + np.random.normal(0, 2.0), 1) for d in days]
        hexyl_acetate = [round(15.0 + 85.0 / (1.0 + np.exp(-0.8 * (d - 4))) + np.random.normal(0, 1.5), 1) for d in days]
        return pd.DataFrame({
            "Ripening_Days": days,
            "Hexanal_Green_(ug/kg)": hexanal,
            "Hexyl_Acetate_Fruity_(ug/kg)": hexyl_acetate
        })

    def generate_peptide_hydrolysis(self):
        """7. 蛋白质定向酶解与活性肽制备 (水解度 DH 与 ACE 抑制率)"""
        times = [10, 30, 60, 90, 120, 180]
        dh = [round(5.0 + 12.0 * (t / (30.0 + t)) + np.random.normal(0, 0.3), 1) for t in times]
        ace = [round(20.0 + 65.0 * (t / (40.0 + t)) + np.random.normal(0, 1.0), 1) for t in times]
        return pd.DataFrame({
            "Hydrolysis_Time_(min)": times,
            "DH_(%)": dh,
            "ACE_Inhibition_(%)": ace
        })

    def get_dataset(self, module_idx):
        handlers = {
            0: self.generate_ppo_kinetics,
            1: self.generate_meat_aging,
            2: self.generate_maillard,
            3: self.generate_lipid_oxidation,
            4: self.generate_fermentation,
            5: self.generate_flavor,
            6: self.generate_peptide_hydrolysis
        }
        return handlers.get(module_idx, self.generate_ppo_kinetics)()

CASE_DATA_ENGINE = {
    0: {"x": "Substrate_mM", "kws": ["PPO", "Cu2+", "Km", "Vmax", "Competitive Inhibition"]},
    1: {"x": "Aging_Days", "kws": ["Calpain", "Cathepsin", "Desmin", "Myofibrillar", "Tenderness"]},
    2: {"x": "Temperature_(C)", "kws": ["Asparagine", "Maillard", "Acrylamide", "Strecker", "Asparaginase"]},
    3: {"x": "Storage_Days", "kws": ["LOX", "Free Radical", "ROOH", "MDA", "Antioxidant"]},
    4: {"x": "Fermentation_Hours", "kws": ["Lactic Acid Bacteria", "EMP Pathway", "Bacteriocin", "pH", "SCFA"]},
    5: {"x": "Ripening_Days", "kws": ["Lipoxygenase", "ADH", "AAT", "Esters", "Flavor Precursor"]},
    6: {"x": "Hydrolysis_Time_(min)", "kws": ["Protease", "Hydrolysis Degree (DH)", "ACE Inhibition", "Bioactive Peptide", "Cleavage Site"]}
}