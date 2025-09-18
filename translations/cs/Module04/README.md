<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-18T16:52:00+00:00",
  "source_file": "Module04/README.md",
  "language_code": "cs"
}
-->
# Kapitola 04: Konverze formátů modelů a kvantizace - Přehled kapitoly

Vzestup EdgeAI učinil konverzi formátů modelů a kvantizaci klíčovými technologiemi pro nasazení pokročilých schopností strojového učení na zařízeních s omezenými zdroji. Tato komplexní kapitola poskytuje kompletní průvodce k pochopení, implementaci a optimalizaci modelů pro scénáře nasazení na okraji.

## 📚 Struktura kapitoly a učební cesta

Tato kapitola je rozdělena do šesti postupných sekcí, které na sebe navazují a vytvářejí komplexní pochopení optimalizace modelů pro edge computing:

---

## [Sekce 1: Základy konverze formátů modelů a kvantizace](./01.Introduce.md)

### 🎯 Přehled
Tato úvodní sekce stanovuje teoretický rámec pro optimalizaci modelů v prostředí edge computingu, pokrývá hranice kvantizace od 1-bitové po 8-bitovou přesnost a klíčové strategie konverze formátů.

**Klíčová témata:**
- Rámec klasifikace přesnosti (ultra-nízká, nízká, střední přesnost)
- Výhody a případy použití formátů GGUF a ONNX
- Přínosy kvantizace pro provozní efektivitu a flexibilitu nasazení
- Výkonnostní benchmarky a porovnání paměťových nároků

**Výsledky učení:**
- Pochopit hranice a klasifikace kvantizace
- Identifikovat vhodné techniky konverze formátů
- Naučit se pokročilé strategie optimalizace pro nasazení na okraji

---

## [Sekce 2: Průvodce implementací Llama.cpp](./02.Llamacpp.md)

### 🎯 Přehled
Komplexní návod k implementaci Llama.cpp, výkonného C++ frameworku umožňujícího efektivní inference velkých jazykových modelů s minimálním nastavením na různých hardwarových konfiguracích.

**Klíčová témata:**
- Instalace na platformách Windows, macOS a Linux
- Konverze formátu GGUF a různé úrovně kvantizace (Q2_K až Q8_0)
- Hardwarová akcelerace pomocí CUDA, Metal, OpenCL a Vulkan
- Integrace s Pythonem a strategie nasazení do produkce

**Výsledky učení:**
- Ovládnout instalaci napříč platformami a sestavení ze zdroje
- Implementovat techniky kvantizace a optimalizace modelů
- Nasadit modely v serverovém režimu s integrací REST API

---

## [Sekce 3: Optimalizační sada Microsoft Olive](./03.MicrosoftOlive.md)

### 🎯 Přehled
Průzkum Microsoft Olive, nástroje pro optimalizaci modelů s ohledem na hardware, který obsahuje více než 40 vestavěných optimalizačních komponent, navržených pro nasazení modelů na podnikové úrovni na různých hardwarových platformách.

**Klíčová témata:**
- Funkce automatické optimalizace s dynamickou a statickou kvantizací
- Inteligence zaměřená na hardware pro nasazení na CPU, GPU a NPU
- Podpora populárních modelů (Llama, Phi, Qwen, Gemma) ihned po instalaci
- Podniková integrace s Azure ML a produkčními pracovními postupy

**Výsledky učení:**
- Využít automatizovanou optimalizaci pro různé architektury modelů
- Implementovat strategie nasazení napříč platformami
- Vytvořit optimalizační pipeline připravené pro podnikové nasazení

---

## [Sekce 4: Optimalizační sada OpenVINO Toolkit](./04.openvino.md)

### 🎯 Přehled
Komplexní průzkum OpenVINO toolkit od Intelu, open-source platformy pro nasazení výkonných AI řešení napříč cloudem, on-premises a edge prostředími s pokročilými schopnostmi Neural Network Compression Framework (NNCF).

**Klíčová témata:**
- Nasazení napříč platformami s hardwarovou akcelerací (CPU, GPU, VPU, AI akcelerátory)
- Neural Network Compression Framework (NNCF) pro pokročilou kvantizaci a prořezávání
- OpenVINO GenAI pro optimalizaci a nasazení velkých jazykových modelů
- Schopnosti podnikových modelových serverů a škálovatelné strategie nasazení

**Výsledky učení:**
- Ovládnout pracovní postupy konverze a optimalizace modelů v OpenVINO
- Implementovat pokročilé techniky kvantizace pomocí NNCF
- Nasadit optimalizované modely na různých hardwarových platformách pomocí Model Serveru

---

## [Sekce 5: Hloubkový průzkum Apple MLX Framework](./05.AppleMLX.md)

### 🎯 Přehled
Komplexní pokrytí Apple MLX, revolučního frameworku speciálně navrženého pro efektivní strojové učení na Apple Silicon, s důrazem na schopnosti velkých jazykových modelů a lokální nasazení.

**Klíčová témata:**
- Výhody jednotné paměťové architektury a Metal Performance Shaders
- Podpora modelů LLaMA, Mistral, Phi-3, Qwen a Code Llama
- LoRA jemné ladění pro efektivní přizpůsobení modelů
- Integrace s Hugging Face a podpora kvantizace (4-bitová a 8-bitová)

**Výsledky učení:**
- Ovládnout optimalizaci pro nasazení LLM na Apple Silicon
- Implementovat techniky jemného ladění a přizpůsobení modelů
- Vytvořit podnikové AI aplikace s rozšířenými funkcemi ochrany soukromí

---

## [Sekce 6: Syntéza pracovního postupu vývoje Edge AI](./06.workflow-synthesis.md)

### 🎯 Přehled
Komplexní syntéza všech optimalizačních frameworků do jednotných pracovních postupů, rozhodovacích matic a osvědčených postupů pro nasazení Edge AI připravené pro produkci napříč různými platformami a případy použití.

**Klíčová témata:**
- Jednotná architektura pracovního postupu integrující více optimalizačních frameworků
- Rozhodovací stromy pro výběr frameworku a analýza kompromisů výkonu
- Validace připravenosti pro produkci a komplexní strategie nasazení
- Strategie budoucí odolnosti pro vznikající hardware a architektury modelů

**Výsledky učení:**
- Ovládnout systematický výběr frameworku na základě požadavků a omezení
- Implementovat produkční pipeline Edge AI s komplexním monitorováním
- Navrhnout přizpůsobitelné pracovní postupy, které se vyvíjejí s novými technologiemi a požadavky

---

## 🎯 Výsledky učení kapitoly

Po dokončení této komplexní kapitoly čtenáři dosáhnou:

### **Technické znalosti**
- Hluboké pochopení hranic kvantizace a praktických aplikací
- Praktické zkušenosti s více optimalizačními frameworky
- Dovednosti pro nasazení v prostředí edge computingu

### **Strategické porozumění**
- Schopnosti výběru optimalizace s ohledem na hardware
- Informované rozhodování o kompromisech výkonu
- Strategie nasazení a monitorování připravené pro podnikové prostředí

### **Výkonnostní benchmarky**

| Framework | Kvantizace | Paměťová náročnost | Zlepšení rychlosti | Případ použití |
|-----------|------------|--------------------|--------------------|----------------|
| Llama.cpp | Q4_K_M     | ~4GB              | 2-3x              | Nasazení napříč platformami |
| Olive     | INT4       | 60-75% snížení    | 2-6x              | Podnikové pracovní postupy |
| OpenVINO  | INT8/INT4  | 50-75% snížení    | 2-5x              | Optimalizace pro hardware Intel |
| MLX       | 4-bit      | ~4GB              | 2-4x              | Optimalizace pro Apple Silicon |

## 🚀 Další kroky a pokročilé aplikace

Tato kapitola poskytuje kompletní základ pro:
- Vývoj vlastních modelů pro specifické obory
- Výzkum v oblasti optimalizace Edge AI
- Vývoj komerčních AI aplikací
- Velkoplošné podnikové nasazení Edge AI

Znalosti z těchto šesti sekcí nabízejí komplexní sadu nástrojů pro orientaci v rychle se vyvíjejícím prostředí optimalizace a nasazení modelů Edge AI.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.