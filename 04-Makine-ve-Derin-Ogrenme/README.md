# 🛠 Kestirimci Bakım: Sensör Verisinden Makine Arızası Tahmini

**Makine ve Derin Öğrenme Uygulamaları · Fatih Okur · 2026**

[![Colab'da Aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FatihOkur/Software-Persona-Projects/blob/main/04-Makine-ve-Derin-Ogrenme/kestirimci_bakim.ipynb)

**Veri:** [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) (UCI, CC BY 4.0). 10.000 örnek, %3,39 arıza.

| Model (test) | Precision | Recall | F1 | PR-AUC |
|---|---|---|---|---|
| Lojistik Regresyon | 0,382 | 0,569 | 0,457 | 0,461 |
| **Random Forest** | **0,978** | **0,863** | **0,917** | **0,939** |
| MLP (PyTorch) | 0,744 | 0,627 | 0,681 | 0,779 |

- Arıza modu sütunları veri sızıntısını önlemek için modelden çıkarıldı.
- Fiziksel özellik mühendisliği (güç, sıcaklık farkı, zorlanma), RF'nin F1 değerini 0,718'den 0,917'ye çıkardı.
- Kaçırılan 7 arızanın 4'ü takım aşınması (TWF) kaynaklı.

📄 Rapor: [`rapor/rapor.pdf`](rapor/rapor.pdf) · 📓 Not defteri: [`kestirimci_bakim.ipynb`](kestirimci_bakim.ipynb)
