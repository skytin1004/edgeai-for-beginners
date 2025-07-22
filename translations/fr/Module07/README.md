<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f921854683b0ba903972831f6e61c28f",
  "translation_date": "2025-07-22T05:23:56+00:00",
  "source_file": "Module07/README.md",
  "language_code": "fr"
}
-->
# Chapitre 07 : Exemples d'EdgeAI

L'Edge AI représente la convergence de l'intelligence artificielle et du calcul en périphérie, permettant un traitement intelligent directement sur les appareils sans dépendre de la connectivité au cloud. Ce chapitre explore cinq implémentations distinctes d'EdgeAI sur différentes plateformes et frameworks, mettant en avant la polyvalence et la puissance des modèles d'IA exécutés en périphérie.

## 1. EdgeAI avec NVIDIA Jetson Orin Nano

Le NVIDIA Jetson Orin Nano marque une avancée majeure dans le domaine de l'Edge AI accessible, offrant jusqu'à 67 TOPS de performance IA dans un format compact de la taille d'une carte de crédit. Cette plateforme puissante démocratise le développement d'IA générative pour les amateurs, les étudiants et les développeurs professionnels.

### Caractéristiques principales
- Offre jusqu'à 67 TOPS de performance IA, soit une amélioration de 1,7X par rapport à son prédécesseur
- 1024 cœurs CUDA et jusqu'à 32 cœurs Tensor pour le traitement IA
- Processeur Arm Cortex-A78AE v8.2 64 bits à 6 cœurs avec une fréquence maximale de 1,5 GHz
- Disponible à seulement 249 $, offrant aux développeurs, étudiants et créateurs une plateforme abordable et accessible

### Applications
Le Jetson Orin Nano excelle dans l'exécution de modèles modernes d'IA générative, notamment les vision transformers, les grands modèles de langage et les modèles vision-langage. Conçu spécifiquement pour les cas d'utilisation de l'IA générative, il permet désormais d'exécuter plusieurs LLMs sur un appareil de la taille de la paume. Les cas d'utilisation populaires incluent la robotique alimentée par l'IA, les drones intelligents, les caméras intelligentes et les appareils autonomes en périphérie.

**En savoir plus** : [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI dans les applications mobiles avec .NET MAUI et ONNX Runtime GenAI

Cette solution montre comment intégrer l'IA générative et les grands modèles de langage (LLMs) dans des applications mobiles multiplateformes en utilisant .NET MAUI (Multi-platform App UI) et ONNX Runtime GenAI. Cette approche permet aux développeurs .NET de créer des applications mobiles sophistiquées alimentées par l'IA, fonctionnant nativement sur les appareils Android et iOS.

### Caractéristiques principales
- Basé sur le framework .NET MAUI, offrant une base de code unique pour les applications Android et iOS
- Intégration d'ONNX Runtime GenAI permettant d'exécuter des modèles d'IA générative directement sur les appareils mobiles
- Prend en charge divers accélérateurs matériels adaptés aux appareils mobiles, y compris CPU, GPU et processeurs IA spécialisés
- Optimisations spécifiques à la plateforme comme CoreML pour iOS et NNAPI pour Android via ONNX Runtime
- Implémente la boucle complète de l'IA générative, y compris le prétraitement, l'inférence, le traitement des logits, la recherche et l'échantillonnage, ainsi que la gestion du cache KV

### Avantages pour les développeurs
L'approche .NET MAUI permet aux développeurs de tirer parti de leurs compétences existantes en C# et .NET tout en créant des applications IA multiplateformes. Le framework ONNX Runtime GenAI prend en charge plusieurs architectures de modèles, notamment Llama, Mistral, Phi, Gemma, et bien d'autres. Les noyaux ARM64 optimisés accélèrent la multiplication matricielle quantifiée INT4, garantissant des performances efficaces sur le matériel mobile tout en maintenant une expérience de développement familière en .NET.

### Cas d'utilisation
Cette solution est idéale pour les développeurs souhaitant créer des applications mobiles alimentées par l'IA en utilisant les technologies .NET, notamment des chatbots intelligents, des applications de reconnaissance d'images, des outils de traduction linguistique et des systèmes de recommandation personnalisés fonctionnant entièrement sur l'appareil pour une confidentialité accrue et une capacité hors ligne.

**En savoir plus** : [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI dans Azure avec Small Language Models Engine

La solution EdgeAI basée sur Azure de Microsoft se concentre sur le déploiement efficace de Small Language Models (SLMs) dans des environnements hybrides cloud-périphérie. Cette approche comble le fossé entre les services d'IA à l'échelle du cloud et les exigences de déploiement en périphérie.

### Avantages de l'architecture
- Intégration transparente avec les services Azure AI
- Exécution des SLMs/LLMs et des modèles multimodaux sur l'appareil et dans le cloud avec ONNX Runtime
- Optimisé pour les déploiements à l'échelle de l'entreprise
- Prise en charge des mises à jour et de la gestion continues des modèles

### Cas d'utilisation
L'implémentation Azure EdgeAI excelle dans les scénarios nécessitant un déploiement IA de niveau entreprise avec des capacités de gestion cloud. Cela inclut le traitement intelligent de documents, l'analyse en temps réel et les flux de travail IA hybrides exploitant à la fois les ressources cloud et périphériques.

**En savoir plus** : [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI avec Windows ML

Windows ML représente le runtime de pointe de Microsoft, optimisé pour une inférence de modèles performante sur l'appareil et un déploiement simplifié, servant de fondation à Windows AI Foundry. Cette plateforme permet aux développeurs de créer des applications Windows alimentées par l'IA, exploitant tout le potentiel du matériel PC.

### Capacités de la plateforme
- Fonctionne sur tous les PC Windows 11 exécutant la version 24H2 (build 26100) ou supérieure
- Compatible avec tout le matériel PC x64 et ARM64, même les PC sans NPU ou GPU
- Permet aux développeurs d'apporter leurs propres modèles et de les déployer efficacement sur l'écosystème des partenaires silicium, y compris AMD, Intel, NVIDIA et Qualcomm, couvrant CPU, GPU, NPU
- Grâce aux APIs d'infrastructure, les développeurs n'ont plus besoin de créer plusieurs versions de leur application pour cibler différents matériels

### Avantages pour les développeurs
Windows ML abstrait le matériel et les fournisseurs d'exécution, vous permettant de vous concentrer sur l'écriture de votre code. De plus, Windows ML se met automatiquement à jour pour prendre en charge les derniers NPUs, GPUs et CPUs dès leur sortie. La plateforme offre un cadre unifié pour le développement IA sur l'écosystème matériel diversifié de Windows.

**En savoir plus** : [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)

## 5. EdgeAI avec Foundry Local Applications

Foundry Local permet aux développeurs de créer des applications de génération augmentée par récupération (RAG) en utilisant des ressources locales dans .NET, combinant des modèles de langage locaux avec des capacités de recherche sémantique. Cette approche offre des solutions IA axées sur la confidentialité, fonctionnant entièrement sur une infrastructure locale.

### Architecture technique
- Combine le modèle de langage Phi-3, les embeddings locaux et le Semantic Kernel pour créer un scénario RAG
- Utilise des embeddings comme vecteurs (tableaux) de valeurs en virgule flottante représentant le contenu et sa signification sémantique
- Semantic Kernel agit comme l'orchestrateur principal, intégrant Phi-3 et les composants intelligents pour créer un pipeline RAG fluide
- Prise en charge des bases de données vectorielles locales, y compris SQLite et Qdrant

### Avantages de l'implémentation
RAG, ou génération augmentée par récupération, est simplement une manière élégante de dire "rechercher des informations et les intégrer dans l'invite". Cette implémentation locale garantit la confidentialité des données tout en fournissant des réponses intelligentes basées sur des bases de connaissances personnalisées. L'approche est particulièrement précieuse pour les scénarios d'entreprise nécessitant la souveraineté des données et des capacités de fonctionnement hors ligne.

**En savoir plus** : [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Conclusion

Ces cinq implémentations d'EdgeAI démontrent la maturité et la diversité des solutions d'IA en périphérie disponibles aujourd'hui. Des appareils périphériques accélérés par le matériel comme le Jetson Orin Nano aux frameworks logiciels comme ONNX Runtime GenAI et Windows ML, les développeurs disposent d'options sans précédent pour déployer des applications intelligentes en périphérie.

Le fil conducteur de toutes ces plateformes est la démocratisation des capacités d'IA, rendant l'apprentissage automatique sophistiqué accessible aux développeurs de différents niveaux de compétence et cas d'utilisation. Que ce soit pour créer des applications mobiles, des logiciels de bureau ou des systèmes embarqués, ces solutions EdgeAI fournissent la base pour la prochaine génération d'applications intelligentes fonctionnant efficacement et en toute confidentialité en périphérie.

Chaque plateforme offre des avantages uniques : Jetson Orin Nano pour le calcul périphérique accéléré par le matériel, ONNX Runtime GenAI pour le développement mobile multiplateforme, Azure EdgeAI pour l'intégration cloud-périphérie d'entreprise, Windows ML pour les applications natives Windows, et Foundry Local pour les implémentations RAG axées sur la confidentialité. Ensemble, elles représentent un écosystème complet pour le développement EdgeAI.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.