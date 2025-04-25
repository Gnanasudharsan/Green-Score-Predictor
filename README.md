# Green-Score-Predictor
The Green Score Predictor estimates the environmental impact of training AI models. By inputting details like model type, dataset size, and hardware used, the tool calculates energy consumption and CO₂ emissions, assigns a Green Score (A–E), and suggests greener alternatives to promote sustainable AI development.

---

# Green Score Predictor for AI Models 🌱

## Abstract

As machine learning models grow in size and complexity, their energy consumption and carbon footprint have become major concerns. The **Green Score Predictor** aims to empower AI developers, researchers, and engineers to make more **sustainable AI** decisions. By estimating the energy consumption and carbon impact of various machine learning models based on training parameters (such as hardware used, dataset size, and training time), this tool helps users understand and minimize their AI models' environmental impact. The app also provides actionable suggestions for optimizing the model’s green score by recommending energy-efficient alternatives.

---

## Problem Statement

With the rapid advancements in AI, training large models (such as GPT, BERT, etc.) has become a significant contributor to energy consumption, resulting in a growing carbon footprint. Despite the importance of environmental sustainability, many AI practitioners are unaware of the energy costs involved in training their models. This lack of visibility makes it difficult to make informed decisions about resource-efficient AI model training.

---

## Output

The **Green Score Predictor** outputs the following results:
- **Estimated Energy Usage** in kilowatt-hours (kWh)
- **Estimated CO₂ Emissions** in kilograms (kg CO₂e)
- **Green Score** (A–E) indicating the sustainability of the model
- **Optimization Suggestions**:
  - Energy-efficient model alternatives (e.g., switching from BERT to DistilBERT)
  - Hardware usage optimizations

---

## Target Customers

- **AI Researchers & Engineers**: Who want to reduce the environmental impact of their machine learning projects.
- **AI Practitioners & Developers**: Developers who want an easy way to estimate the carbon footprint of their models.
- **Academia & Universities**: For educational purposes, showcasing the impact of AI models on the environment.
- **Tech Companies**: Companies looking to integrate sustainability practices into their AI development pipelines.

---

## Potential Users Who Will Utilize This More

- **Sustainability-focused AI teams**: Working towards reducing energy costs and improving the green credentials of AI.
- **Data Centers and Cloud Providers**: Wanting to benchmark and optimize the carbon impact of AI models running on their infrastructure.
- **Researchers in Environmental AI**: Looking for tools to evaluate and optimize AI models for green energy consumption.

---

## How to Run This Code

To run the **Green Score Predictor** locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/gnanasudharsan/green-score-predictor.git
cd green-score-predictor
```

### 2. Install Dependencies

Ensure you have Python installed. Then, install the required Python libraries:

```bash
pip install -r requirements.txt
```

Alternatively, you can install the dependencies individually:

```bash
pip install streamlit codecarbon pandas
```

### 3. Run the Streamlit App

After installing the dependencies, run the app:

```bash
streamlit run Green_Score_Predictor.py
```

### 4. Access the Web App

Once the app is running, it will open a new page in your browser at `http://localhost:8501`. You can now start using the **Green Score Predictor**!

---

## How It Works

1. **User Inputs**:
   - Users input key parameters such as the **model type**, **dataset size**, **training duration**, **hardware used**, and **number of devices**.
   
2. **Emissions Calculation**:
   - Based on the selected hardware (CPU/GPU/TPU) and model type, the app estimates the **energy consumption** in kilowatt-hours (kWh) and the corresponding **CO₂ emissions** using simple formulas or external tools like **CodeCarbon**.

3. **Green Score**:
   - The tool calculates a **Green Score (A-E)** based on the emissions and suggests optimizations for reducing the carbon footprint, such as recommending smaller models or using different hardware.

4. **Results & Suggestions**:
   - Once the results are generated, users are provided with actionable insights and model alternatives that can help reduce their environmental impact.

---

## Future Enhancements

- Integration with more **hardware benchmarks** for more accurate emission predictions.
- Ability to **compare multiple models** side by side for a more detailed analysis.
- Expand emission calculators to support additional metrics like **data center efficiency** or **cloud energy**.
- Enable **exporting results** to CSV or PDF for documentation purposes.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---
