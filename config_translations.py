# -*- coding: utf-8 -*-
"""
PMSA-FoodBiochem System Internationalization & Corpus Configuration Module
Filename: config_translations.py
Description: Multi-language dictionaries, case corpus, and UI texts focusing on Food Biochemistry.
"""

TRANSLATIONS = {
    "zh": {
        "title": "🔬 PMSA-食品生物化学 AI 智慧学习工作站 V1.0",
        "sub": "由 PMSA 教学模型驱动的食品生物化学高阶思维、代谢通路与过程性评价平台",
        "lang_label": "🌐 切换系统语言 / Language",
        "lbl_case": "🌟 1. 选择探究章节模块:",
        "lbl_step": "🧭 2. PMSA 教学流程环节:",
        "logout_btn": "退出当前系统",
        "p_bg": "📖 Problem - 生物化学工业背景与研究痛点",
        "p_focus": "🔬 动态大分子与生化代谢焦点",
        "p_task": "🎯 核心生化挑战与高阶任务目标",
        "p_task_1": (
            "* **任务 1:** 解析核心食品生化代谢/转化机制并提出科学假设。\n"
            "* **任务 2:** 深度解构酶动力学与代谢通路数据集趋势。"
        ),
        "p_download_btn": "📥 下载该模块标准生化数据集模板",
        "m_title": "Mechanism - 生物化学分子机制与通路图谱建构",
        "m_keyword_lbl": "⚠️ 核心生化机制关键词/内源酶/代谢通路守卫:",
        "m_lbl": "请梳理该食品生物化学变化/代谢反应的底层分子机制链条:",
        "m_holder": (
            "例如：底物结合酶活性中心 -> 生成中间产物 -> 自由基夺氢链式反应 -> "
            "产生挥发性醛酮类或聚合物..."
        ),
        "m_btn": "提交生化机制链条并生成多维诊断",
        "m_success": "✅ 生化机制处理完成！过程性评价痕迹已成功上传至 WPS 云端痕迹表。",
        "s_title": "Simulation - 酶动力学与生化代谢数据挖掘区",
        "s_upload": "📤 上传您个人的实验原始数据集 (支持 CSV/XLSX)",
        "s_preview": "生化数据矩阵快照:",
        "a_title": "Application - 食品生物技术创新与质量调控方案提报区",
        "a_task_lbl": "💡 当前模块核心任务：",
        "a_intro": (
            "请结合在前几个阶段梳理的生物化学机制与动力学仿真趋势，完成以下结构化的食品生物技术改良与调控方案设计："
        ),
        "a_part1": "📝 第一部分：生物技术创新方案基本信息",
        "a_p1_name": "✨ 1. 方案创新名称:",
        "a_p1_name_holder": "例如：基于复配植物多酚定向抑制果蔬多酚氧化酶（PPO）的绿色保鲜技术",
        "a_p1_route": "🛠️ 2. 核心生物技术路径分类:",
        "a_routes": [
            "酶促反应与动力学调控",
            "内源酶激活与肉质重塑",
            "糖代谢途径与加成抑制",
            "脂质自由基过氧化与清除",
            "发酵微生态与代谢生物转化",
            "风味前体生物合成与转化",
            "蛋白定向酶解与活性肽制备"
        ],
        "a_part2": "🔬 第二部分：高阶生物工程设计规范",
        "a_t1_lbl": "🎯 任务 1：核心生化调控参数与工艺设计",
        "a_t1_cap": "请具体列出生物技术调控参数（如酶用量、底物浓度、pH、温度、专一性抑制剂添加量或发酵条件等）。",
        "a_t1_holder": "例：添加0.05%柠檬酸（调pH至4.0）配合0.02%绿原酸，在4℃下处理果肉，降低PPO对底物的结合亲和力...",
        "a_t2_lbl": "🧬 任务 2：方案背后的生物化学与代谢机制阐述",
        "a_t2_cap": "请简述你采用的上述生物技术，是如何在蛋白质/内源酶/代谢通路层面上调控食品品质或抑制劣变的？",
        "a_t2_holder": "例：柠檬酸通过螯合PPO活性中心铜离子（Cu2+）降低酶活；低pH导致PPO空间构象改变，提高催化活化能...",
        "a_t3_lbl": "📊 任务 3：生化指标监测与品质验证评价体系",
        "a_t3_cap": "你计划测定哪些关键生化指标（如相对酶活、MDA含量、水解度DH、风味前体量）来验证方案？",
        "a_t3_holder": "例：测定处理组与对照组在储藏期内的PPO相对活性、褐变指数（A420）、总酚含量及游离氨基酸组分...",
        "a_part3": "📤 第三部分：附件与最终提报",
        "a_file_lbl": "📎 上传更详尽的生化实验设计书/正交试验图表/PDF报告 (可选)",
        "a_submit_btn": "🚀 提交最终食品生物技术调控方案",
        "a_success": "🎉 方案提报成功！学术数据已安全发射至班级过程性看板并实时同步至 WPS。",
        "an_title": "Analytics - 智能评价与过程性学习画像看板",
        "an_no_data": "⚠️ 目前云端看板暂无活跃行为留痕。当学生在前方点击提交后，这里会立刻激活数智化画像。",
        "an_user_logs": "历史学习与提交痕迹清单",
        "metric_1": "生化机制建构深度",
        "metric_2": "代谢数据主张力",
        "metric_3": "生物技术创新性",
        "cases": [
            "1. 酶促反应与酶动力学调控 (Enzymatic Browning & Kinetics)",
            "2. 内源酶与肌肉食品采后成熟 (Endogenous Enzymes & Post-mortem Aging)",
            "3. 糖类代谢途径与美拉德变化 (Carbohydrate Metabolism & Maillard)",
            "4. 脂质自由基过氧化与酶促氧化 (Lipid Bio-oxidation & Free Radicals)",
            "5. 食品发酵微生态与代谢转化 (Food Fermentation & Biotransformation)",
            "6. 风味前体物的生物合成与转化 (Flavor Precursor Biogenesis)",
            "7. 蛋白质定向酶解与活性肽制备 (Proteolysis & Bioactive Peptides)"
        ],
        "steps": [
            "Problem 科学情境",
            "Mechanism 机制建构",
            "Simulation 数据分析",
            "Application 方案应用",
            "Analytics 智能评价"
        ]
    },
    "en": {
        "title": "🔬 PMSA-FoodBiochem AI Learning Workstation V1.0",
        "sub": "A PMSA-driven platform for higher-order thinking, metabolic pathways, & formative assessment",
        "lang_label": "🌐 Switch System Language",
        "lbl_case": "🌟 1. Select Chapter Module:",
        "lbl_step": "🧭 2. PMSA Pedagogical Stage:",
        "logout_btn": "Sign Out System",
        "p_bg": "📖 Problem - Food Biochemistry Industrial Background & Research Bottlenecks",
        "p_focus": "🔬 Biochemical Mechanism & Metabolic Focus",
        "p_task": "🎯 Core Biochemical Challenges & Task Objectives",
        "p_task_1": (
            "* **Task 1:** Parse core food biochemical conversion mechanisms and formulate hypotheses.\n"
            "* **Task 2:** Deconstruct enzyme kinetics and metabolic dataset trends."
        ),
        "p_download_btn": "📥 Download Standard Biochemical Dataset Template",
        "m_title": "Mechanism - Biochemical Mechanism & Pathway Mapping",
        "m_keyword_lbl": "⚠️ Core Biochemical Keywords / Endogenous Enzymes / Pathways Guard:",
        "m_lbl": "Map the underlying biochemical mechanism or metabolic pathway of the food phenomenon:",
        "m_holder": "e.g., Substrate binds to active site -> Intermediate formation -> Radical chain reaction...",
        "m_btn": "Submit Mechanism Map for Multidimensional Diagnosis",
        "m_success": "✅ Biochemical mechanism processing complete! Data synchronized with WPS Cloud.",
        "s_title": "Simulation - Enzyme Kinetics & Metabolic Data Mining",
        "s_upload": "📤 Upload Your Empirical Dataset (Supports CSV/XLSX)",
        "s_preview": "Biochemical Data Matrix Snapshot:",
        "a_title": "Application - Food Biotechnology Innovation & Quality Control Scheme",
        "a_task_lbl": "💡 Core Task for Current Module:",
        "a_intro": "Combine the biochemical mechanisms and kinetic trends explored in previous stages:",
        "a_part1": "Part I: Basic Biotechnology Project Information",
        "a_p1_name": "✨ 1. Project Innovation Title:",
        "a_p1_name_holder": "e.g., Green preservation via Polyphenol-based PPO kinetics inhibition",
        "a_p1_route": "🛠️ 2. Core Technological Route Classification:",
        "a_routes": [
            "Enzyme Kinetics Control",
            "Endogenous Enzymes & Aging",
            "Carbohydrate Pathways",
            "Lipid Oxidation & Radical Clearance",
            "Fermentation & Biotransformation",
            "Flavor Precursor Biogenesis",
            "Enzymatic Hydrolysis & Peptides"
        ],
        "a_part2": "🔬 Part II: Higher-Order Bio-Engineering Specifications",
        "a_t1_lbl": "🎯 Task 1: Core Biochemical Control Parameters & Process Design",
        "a_t1_cap": "Specify biotechnology parameters (e.g., enzyme dosage, pH, temperature, substrate conc).",
        "a_t1_holder": "e.g., Add 0.05% citric acid (pH 4.0) with 0.02% chlorogenic acid at 4°C...",
        "a_t2_lbl": "🧬 Task 2: Biochemical & Metabolic Justification",
        "a_t2_cap": "Explain how your approach regulates quality at the protein/pathway level.",
        "a_t2_holder": "e.g., Citric acid chelates Cu2+ at PPO active center; low pH lowers substrate affinity...",
        "a_t3_lbl": "📊 Task 3: Biochemical Monitoring & Quality Evaluation",
        "a_t3_cap": "What key biochemical indicators will you measure to validate the plan?",
        "a_t3_holder": "e.g., Measure relative PPO activity, browning index (A420), and total phenols...",
        "a_part3": "📤 Part III: Attachments & Final Submission",
        "a_file_lbl": "📎 Upload detailed biochemical design, orthogonal charts, or PDF report",
        "a_submit_btn": "🚀 Submit Final Biotechnology Scheme",
        "a_success": "🎉 Submission Successful! Academic footprint synchronously uploaded to WPS.",
        "an_title": "Analytics - Formative Evaluation & Learning Analytics Dashboard",
        "an_no_data": "⚠️ No cloud footprint detected yet. Student activity logs will be rendered automatically.",
        "an_user_logs": "Historical Submissions & Learning Footprints",
        "metric_1": "Biochemical Mapping Depth",
        "metric_2": "Metabolic Argumentation",
        "metric_3": "Biotech Innovation",
        "cases": [
            "1. Enzymatic Browning & Kinetics",
            "2. Endogenous Enzymes & Post-mortem Aging",
            "3. Carbohydrate Metabolism & Maillard",
            "4. Lipid Bio-oxidation & Free Radicals",
            "5. Food Fermentation & Biotransformation",
            "6. Flavor Precursor Biogenesis",
            "7. Proteolysis & Bioactive Peptides"
        ],
        "steps": [
            "Problem Context",
            "Mechanism Mapping",
            "Simulation Analytics",
            "Application Output",
            "Analytics Feedback"
        ]
    }
}

MODULE_DESCRIPTIONS = {
    0: {
        "zh": {
            "problem": "鲜切果蔬加工与储存过程中，多酚氧化酶（PPO）催化酚类底物快速发生酶促褐变，导致品质劣变。如何选择专一性抑制剂进行精准动力学调控？",
            "mechanism": "PPO 活性中心 Cu2+ 催化单酚羟基化和双酚脱氢生成醌 -> 醌类自由基缩合生成黑色素；竞争性/非竞争性抑制剂通过结合活性中心改变 Km 或 Vmax。",
            "application": "针对鲜切苹果或马铃薯，设计一套基于天然多酚/有机酸抑制 PPO 活性与控制酶促褐变的绿色生物保鲜方案。"
        },
        "en": {
            "problem": "During fresh-cut fruit processing, Polyphenol Oxidase (PPO) catalyzes rapid browning. How can we select specific inhibitors via kinetics control?",
            "mechanism": "PPO Cu2+ active site oxidizes phenols to quinones -> Quinones polymerize to melanin; Inhibitors alter Km or Vmax.",
            "application": "Design a green bio-preservation scheme using natural PPO inhibitors for fresh-cut produce."
        }
    },
    1: {
        "zh": {
            "problem": "畜禽屠宰后肌肉发生僵直与成熟，内源钙激活酶（Calpain）与溶酶体酶（Cathepsin）如何动态重塑肌纤维结构并影响肉品的嫩度与持水力？",
            "mechanism": "糖原无氧酵解导致 pH 下降 -> 钙离子释放激活 Calpain -> 选择性降解 Desmin 和 Titin 等肌纤维微结构蛋白 -> 持水力与嫩度发生重塑。",
            "application": "设计一套基于温湿度/离子浓度调控内源酶活性的牛肉/猪肉宰后排毒与精准成熟工艺。"
        },
        "en": {
            "problem": "How do endogenous Calpains and Cathepsins reshape muscle fibril structures and affect meat tenderness/WHC post-mortem?",
            "mechanism": "Post-mortem glycolysis drops pH -> Ca2+ release activates Calpain -> Selective degradation of Desmin/Titin -> Texture & WHC transformation.",
            "application": "Design a post-mortem meat aging process by controlling endogenous enzyme kinetics."
        }
    },
    2: {
        "zh": {
            "problem": "热加工过程中还原糖与氨基酸发生美拉德反应，在赋予食品独特风味与色泽的同时，如何生物化学抑制定量丙烯酰胺（Acrylamide）等毒害产物？",
            "mechanism": "天冬酰胺（Asn）与还原糖羰基进行加成缩合 -> Schiff 碱生成 -> Strecker 降解形成丙烯酰胺；天冬酰胺酶（Asparaginase）可预先阻断此通路。",
            "application": "利用天冬酰胺酶预处理结合加工参数调控，设计低丙烯酰胺、高风味的健康烘焙食品方案。"
        },
        "en": {
            "problem": "Maillard reaction creates flavor but generates toxic acrylamide. How can we biochemically block acrylamide formation?",
            "mechanism": "Asparagine + Reducing sugars -> Schiff base -> Strecker degradation to acrylamide; Asparaginase pre-treatment cleaves Asparagine.",
            "application": "Design a healthy baking scheme using Asparaginase pre-treatment to inhibit acrylamide."
        }
    },
    3: {
        "zh": {
            "problem": "富含不饱和脂肪酸（PUFA）的食品极易发生脂质过氧化，引发哈变风味与丙二醛（MDA）积累。如何通过生物抗氧化机制终止自由基链式反应？",
            "mechanism": "脂氧合酶（LOX）或单线态氧引发自由基 -> 夺氢生成氢过氧化物（ROOH） -> β-裂解生成小分子醛酮；生化抗氧化剂（如生育酚、SOD）提供氢原子清除 ROO•。",
            "application": "针对富含 EPA/DHA 的鱼油或坚果食品，构建多屏障内源/外源生物抗氧化稳定体系。"
        },
        "en": {
            "problem": "Lipid peroxidation of PUFA causes rancidity and toxic MDA. How can radical chain reactions be terminated via antioxidant mechanisms?",
            "mechanism": "LOX/singlet oxygen initiates radicals -> ROOH formation -> beta-scission into aldehydes; Antioxidants donate H-atoms to scavenge ROO•.",
            "application": "Construct a multi-barrier antioxidant system for omega-3 rich marine oils or nuts."
        }
    },
    4: {
        "zh": {
            "problem": "发酵乳/发酵蔬菜中，乳酸菌（LAB）如何利用碳水化合物进行同型/异型乳酸发酵，并产生抑菌肽与风味物质？",
            "mechanism": "EMP/PKP 通路代谢葡萄糖 -> 丙酮酸还原为乳酸（降低pH） -> 产生短链脂肪酸（SCFA）与细菌素（Bacteriocin） -> 抑制致病菌并重塑凝胶结构。",
            "application": "设计一款基于多菌种共生发酵的益生菌功能性发酵食品及其生物转化工艺。"
        },
        "en": {
            "problem": "How do Lactic Acid Bacteria convert carbs via lactic fermentation to generate flavor and bacteriocins?",
            "mechanism": "EMP/PKP pathways metabolize glucose to lactic acid -> pH drops -> Production of SCFAs and bacteriocins -> Pathogen inhibition & gelation.",
            "application": "Design a probiotic functional fermented food using co-culture fermentation technology."
        }
    },
    5: {
        "zh": {
            "problem": "水果采后成熟或茶树鲜叶加工过程中，关键香气物质（如青香、果香）是如何由脂质和氨基酸前体生物合成的？",
            "mechanism": "亚麻酸/亚油酸 -> LOX 与氢过氧化物裂解酶（HPL）催化 -> C6/C9 绿叶醛酮 -> 醇脱氢酶（ADH）与醇酰基转移酶（AAT）转化生成挥发性酯类。",
            "application": "开发一套调控果蔬采后风味酶（ADH/AAT）表达与前体转化的香气保全/增香技术。"
        },
        "en": {
            "problem": "How are volatile flavor compounds biosynthesized from lipid and amino acid precursors during fruit ripening?",
            "mechanism": "Linolenic acid -> LOX & HPL catalysis -> C6/C9 aldehydes -> ADH & AAT catalysis to volatile esters.",
            "application": "Develop a flavor preservation scheme regulating ADH/AAT activity in post-harvest produce."
        }
    },
    6: {
        "zh": {
            "problem": "如何利用特异性蛋白酶（如碱性蛋白酶、胰蛋白酶）定向水解蛋白源，高效切割释放具有降血压（ACE抑制）或抗氧化的生物活性肽？",
            "mechanism": "蛋白酶专一性识别疏水/碱性氨基酸残基肽键 -> 底物开裂暴露活性末端 -> 活性肽与靶点（如ACE酶活性中心）高效结合。",
            "application": "针对大豆蛋白、乳清蛋白或牦牛乳蛋白，设计一套定量控制水解度（DH）与靶向活性肽制备工艺。"
        },
        "en": {
            "problem": "How can specific proteases be used to hydroylze proteins to target bioactive peptides with ACE-inhibitory activity?",
            "mechanism": "Protease recognizes specific peptide bonds -> Cleavage exposes active terminals -> Peptides dock into active sites of target enzymes.",
            "application": "Design a enzymatic hydrolysis process to produce biopeptides with controlled degree of hydrolysis (DH)."
        }
    }
}