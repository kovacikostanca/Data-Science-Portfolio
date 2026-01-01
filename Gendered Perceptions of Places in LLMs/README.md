# Case Study: Whose Perspective Does AI Reflect? 
### Auditing Gendered & Geographical Bias in LLMs vs. Real-World Data

## 📌 Executive Summary
[cite_start]This research investigates whether industry-leading Large Language Models (LLMs)—specifically **GPT-5 and Claude Sonnet 4**—reproduce or amplify gendered stereotypes and geographical biases[cite: 9, 50]. [cite_start]By comparing AI-generated descriptions of London neighborhoods against **1.6M+ Airbnb reviews** and **official crime statistics**, the study identifies a critical "perception gap"[cite: 10, 17, 112]. 

[cite_start]Key findings reveal that while human reviews align closely with ground-truth crime data, LLMs exhibit systematic gender bias, frequently over-labeling female-associated prompts as "safe" (~51%) compared to male prompts (~55%), while simultaneously under-representing overall safety compared to human experience (90% safe in Airbnb vs. ~50% in LLMs)[cite: 38, 40, 45, 95].

## 🛠️ The Tech Stack & Methodology
* [cite_start]**Models Under Test:** GPT-5, Claude Sonnet 4[cite: 50].
* **Data Sources:**
    * [cite_start]**Human Sentiment:** 1.6M+ London Airbnb reviews (2009–2025)[cite: 17, 48].
    * [cite_start]**Ground Truth:** 969,175 official London Crime Rate records (2024–2025)[cite: 17, 49].
    * [cite_start]**Synthetic Data:** 630 systematically engineered LLM prompts across male, female, and neutral personas[cite: 17, 50, 70].
* **Analytical Techniques:**
    * [cite_start]**Topic Modeling:** Utilized **BERTopic** and Prototype-Based Embeddings to categorize descriptions into themes like Safety, Transportation, and Amenities[cite: 61, 64, 65].
    * [cite_start]**Sentiment Analysis:** Comparative safety-sentiment framing and polarity (positive/negative/neutral)[cite: 67, 73].
    * [cite_start]**Fairness Auditing:** Applied **Demographic Parity** and **Equalized Odds** metrics to quantify systemic bias[cite: 76, 77, 78, 106].
    * [cite_start]**Geospatial Analysis:** Ward-level neighborhood mapping and choropleth visualizations to detect geographical bias[cite: 58, 59, 81].



## 🔍 Key Objectives
1. [cite_start]**Identify Nuance:** Determine if LLMs reflect gendered nuances in neighborhood descriptions compared to human reviews[cite: 27].
2. [cite_start]**Safety Alignment:** Evaluate if LLM safety recommendations align with official crime data (Spearman's Rank Correlation)[cite: 28, 81].
3. [cite_start]**Bias Measurement:** Quantify if AI models favor specific gendered perspectives or reinforce stereotypes in travel suggestions[cite: 29].

## 📈 Major Findings & Insights
* [cite_start]**Systematic Gender Bias:** LLMs introduce significant gender bias not present in human data (Claude: $t=3.85, p=0.001$; GPT-5: $t=2.44, p=0.024$)[cite: 98, 108].
* [cite_start]**Weak Ground-Truth Correlation:** Airbnb reviews track crime patterns closely, but LLMs show weak or no correlation, often "hallucinating" or exaggerating risks in low-crime areas[cite: 92, 95, 112].
* [cite_start]**Model Polarity:** LLMs understate safety significantly, describing neighborhoods as safe only ~50% of the time, whereas human residents/travelers report 90% safety[cite: 111].
* [cite_start]**Semantic Divergence:** GPT-5 and Claude only partially reflect human nuances, showing weak semantic alignment with human reviews (Similarity scores: GPT-5 = 0.28, Claude = 0.23)[cite: 15, 110].



## 💡 Impact & Contribution
[cite_start]This project contributes to the field of **AI Fairness** by addressing the underexplored intersection of gender and geography[cite: 11, 114]. [cite_start]It highlights the risks of using unfiltered LLM outputs for social applications like travel recommendations, where biased results can distort community perceptions and affect trust[cite: 114]. [cite_start]The findings advocate for more transparent, responsible AI deployment and the implementation of robust bias detection strategies[cite: 11, 114].

## 📂 Deliverables (What’s in the Repo)
* [cite_start]`/preprocessing`: Scripts for cleaning Airbnb/Crime data and gender extraction (98% accuracy via **Gender-Guesser** and **Genderize.io**)[cite: 52, 53, 56].
* [cite_start]`/prompt_engineering`: Framework for generating gender-stratified LLM responses[cite: 69, 70].
* [cite_start]`/notebooks`: BERTopic modeling, sentiment classification, and statistical evaluation (T-tests, Spearman's correlation)[cite: 60, 64, 75, 80].
* [cite_start]`/visualizations`: Comparative ward-level maps, sentiment distribution charts, and semantic similarity histograms[cite: 13, 23, 81].

---
[cite_start]*This research was submitted as a thesis for the MSc in Data Science at Middlesex University London[cite: 4, 5].*
