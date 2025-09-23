<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-17T13:55:57+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "pt"
}
-->
# AI Toolkit para Visual Studio Code - Guia de Desenvolvimento de Edge AI

## Introdução

Bem-vindo ao guia completo para utilizar o AI Toolkit no Visual Studio Code no desenvolvimento de Edge AI. À medida que a inteligência artificial evolui de computação centralizada na nuvem para dispositivos distribuídos na periferia, os programadores precisam de ferramentas poderosas e integradas que enfrentem os desafios únicos do desenvolvimento na periferia - desde restrições de recursos até requisitos de operação offline.

O AI Toolkit para Visual Studio Code preenche esta lacuna ao oferecer um ambiente de desenvolvimento completo, especificamente projetado para criar, testar e otimizar aplicações de IA que funcionem eficientemente em dispositivos de periferia. Quer esteja a desenvolver para sensores IoT, dispositivos móveis, sistemas embutidos ou servidores de periferia, este toolkit simplifica todo o fluxo de trabalho de desenvolvimento dentro do ambiente familiar do VS Code.

Este guia irá conduzi-lo pelos conceitos essenciais, ferramentas e melhores práticas para aproveitar o AI Toolkit nos seus projetos de Edge AI, desde a seleção inicial de modelos até à implementação em produção.

## Visão Geral

O AI Toolkit oferece um ambiente de desenvolvimento integrado para todo o ciclo de vida de aplicações de Edge AI dentro do VS Code. Ele proporciona integração perfeita com modelos de IA populares de fornecedores como OpenAI, Anthropic, Google e GitHub, enquanto suporta a implementação local de modelos através de ONNX e Ollama - capacidades cruciais para aplicações de Edge AI que requerem inferência no dispositivo.

O que diferencia o AI Toolkit para o desenvolvimento de Edge AI é o seu foco em todo o pipeline de implementação na periferia. Ao contrário das ferramentas tradicionais de desenvolvimento de IA que se concentram principalmente na implementação na nuvem, o AI Toolkit inclui funcionalidades especializadas para otimização de modelos, testes em condições de restrição de recursos e avaliação de desempenho específica para a periferia. O toolkit compreende que o desenvolvimento de Edge AI exige considerações diferentes - tamanhos de modelos menores, tempos de inferência mais rápidos, capacidade offline e otimizações específicas de hardware.

A plataforma suporta múltiplos cenários de implementação, desde inferência simples no dispositivo até arquiteturas complexas de múltiplos modelos na periferia. Ela fornece ferramentas para conversão, quantização e otimização de modelos que são essenciais para uma implementação bem-sucedida na periferia, enquanto mantém a produtividade do programador que o VS Code é conhecido por oferecer.

## Objetivos de Aprendizagem

Ao final deste guia, será capaz de:

### Competências Essenciais
- **Instalar e configurar** o AI Toolkit para Visual Studio Code em fluxos de trabalho de desenvolvimento de Edge AI
- **Navegar e utilizar** a interface do AI Toolkit, incluindo o Catálogo de Modelos, Playground e Agent Builder
- **Selecionar e avaliar** modelos de IA adequados para implementação na periferia com base em desempenho e restrições de recursos
- **Converter e otimizar** modelos utilizando o formato ONNX e técnicas de quantização para dispositivos de periferia

### Competências de Desenvolvimento de Edge AI
- **Projetar e implementar** aplicações de Edge AI utilizando o ambiente de desenvolvimento integrado
- **Realizar testes de modelos** em condições semelhantes à periferia utilizando inferência local e monitorização de recursos
- **Criar e personalizar** agentes de IA otimizados para cenários de implementação na periferia
- **Avaliar o desempenho de modelos** utilizando métricas relevantes para computação na periferia (latência, uso de memória, precisão)

### Otimização e Implementação
- **Aplicar técnicas de quantização e poda** para reduzir o tamanho do modelo enquanto mantém um desempenho aceitável
- **Otimizar modelos** para plataformas de hardware específicas da periferia, incluindo aceleração por CPU, GPU e NPU
- **Implementar melhores práticas** para desenvolvimento de Edge AI, incluindo gestão de recursos e estratégias de fallback
- **Preparar modelos e aplicações** para implementação em produção em dispositivos de periferia

### Conceitos Avançados de Edge AI
- **Integrar com frameworks de Edge AI** como ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementar arquiteturas de múltiplos modelos** e cenários de aprendizagem federada para ambientes de periferia
- **Resolver problemas comuns de Edge AI** como restrições de memória, velocidade de inferência e compatibilidade de hardware
- **Projetar estratégias de monitorização e registo** para aplicações de Edge AI em produção

### Aplicação Prática
- **Construir soluções completas de Edge AI** desde a seleção de modelos até à implementação
- **Demonstrar proficiência** em fluxos de trabalho de desenvolvimento específicos para a periferia e técnicas de otimização
- **Aplicar conceitos aprendidos** a casos de uso reais de Edge AI, incluindo IoT, dispositivos móveis e aplicações embutidas
- **Avaliar e comparar** diferentes estratégias de implementação de Edge AI e os seus compromissos

## Funcionalidades Principais para Desenvolvimento de Edge AI

### 1. Catálogo de Modelos e Descoberta
- **Suporte a Modelos Locais**: Descubra e aceda a modelos de IA especificamente otimizados para implementação na periferia
- **Integração com ONNX**: Aceda a modelos no formato ONNX para inferência eficiente na periferia
- **Suporte a Ollama**: Utilize modelos que funcionam localmente através do Ollama para privacidade e operação offline
- **Comparação de Modelos**: Compare modelos lado a lado para encontrar o equilíbrio ideal entre desempenho e consumo de recursos para dispositivos de periferia

### 2. Playground Interativo
- **Ambiente de Teste Local**: Teste modelos localmente antes da implementação na periferia
- **Experimentação Multimodal**: Teste com imagens, texto e outros inputs típicos em cenários de periferia
- **Ajuste de Parâmetros**: Experimente diferentes parâmetros de modelos para otimizar para restrições da periferia
- **Monitorização de Desempenho em Tempo Real**: Observe a velocidade de inferência e o uso de recursos durante o desenvolvimento

### 3. Agent Builder para Aplicações de Periferia
- **Engenharia de Prompts**: Crie prompts otimizados que funcionem eficientemente com modelos menores na periferia
- **Integração com Ferramentas MCP**: Integre ferramentas do Model Context Protocol para capacidades avançadas de agentes na periferia
- **Geração de Código**: Gere código pronto para produção otimizado para cenários de implementação na periferia
- **Saídas Estruturadas**: Projete agentes que forneçam respostas consistentes e estruturadas adequadas para aplicações na periferia

### 4. Avaliação e Teste de Modelos
- **Métricas de Desempenho**: Avalie modelos utilizando métricas relevantes para implementação na periferia (latência, uso de memória, precisão)
- **Testes em Lote**: Teste múltiplas configurações de modelos simultaneamente para encontrar configurações ideais para a periferia
- **Avaliação Personalizada**: Crie critérios de avaliação personalizados específicos para casos de uso de Edge AI
- **Perfil de Recursos**: Analise requisitos de memória e computação para planeamento de implementação na periferia

### 5. Conversão e Otimização de Modelos
- **Conversão para ONNX**: Converta modelos de vários formatos para ONNX para compatibilidade com a periferia
- **Quantização**: Reduza o tamanho do modelo e melhore a velocidade de inferência através de técnicas de quantização
- **Otimização de Hardware**: Otimize modelos para hardware específico da periferia (CPU, GPU, NPU)
- **Transformação de Formatos**: Transforme modelos de Hugging Face e outras fontes para implementação na periferia

### 6. Ajuste Fino para Cenários de Periferia
- **Adaptação de Domínio**: Personalize modelos para casos de uso e ambientes específicos da periferia
- **Treino Local**: Treine modelos localmente com suporte a GPU para requisitos específicos da periferia
- **Integração com Azure**: Utilize Azure Container Apps para ajuste fino baseado na nuvem antes da implementação na periferia
- **Aprendizagem por Transferência**: Adapte modelos pré-treinados para tarefas e restrições específicas da periferia

### 7. Monitorização e Rastreamento de Desempenho
- **Análise de Desempenho na Periferia**: Monitorize o desempenho de modelos em condições semelhantes à periferia
- **Coleta de Rastreamento**: Colete dados detalhados de desempenho para otimização
- **Identificação de Gargalos**: Identifique problemas de desempenho antes da implementação em dispositivos de periferia
- **Monitorização de Uso de Recursos**: Acompanhe memória, CPU e tempo de inferência para otimização na periferia

## Fluxo de Trabalho de Desenvolvimento de Edge AI

### Fase 1: Descoberta e Seleção de Modelos
1. **Explorar o Catálogo de Modelos**: Utilize o catálogo de modelos para encontrar modelos adequados para implementação na periferia
2. **Comparar Desempenho**: Avalie modelos com base em tamanho, precisão e velocidade de inferência
3. **Testar Localmente**: Utilize modelos Ollama ou ONNX para testar localmente antes da implementação na periferia
4. **Avaliar Requisitos de Recursos**: Determine as necessidades de memória e computação para dispositivos de periferia alvo

### Fase 2: Otimização de Modelos
1. **Converter para ONNX**: Converta modelos selecionados para o formato ONNX para compatibilidade com a periferia
2. **Aplicar Quantização**: Reduza o tamanho do modelo através de quantização INT8 ou INT4
3. **Otimização de Hardware**: Otimize para hardware de periferia alvo (ARM, x86, aceleradores especializados)
4. **Validação de Desempenho**: Valide que os modelos otimizados mantêm precisão aceitável

### Fase 3: Desenvolvimento de Aplicações
1. **Design de Agentes**: Utilize o Agent Builder para criar agentes de IA otimizados para a periferia
2. **Engenharia de Prompts**: Desenvolva prompts que funcionem eficazmente com modelos menores
3. **Testes de Integração**: Teste agentes em condições simuladas de periferia
4. **Geração de Código**: Gere código de produção otimizado para implementação na periferia

### Fase 4: Avaliação e Teste
1. **Avaliação em Lote**: Teste múltiplas configurações para encontrar configurações ideais para a periferia
2. **Perfil de Desempenho**: Analise velocidade de inferência, uso de memória e precisão
3. **Simulação de Periferia**: Teste em condições semelhantes ao ambiente de implementação na periferia
4. **Testes de Stress**: Avalie o desempenho sob várias condições de carga

### Fase 5: Preparação para Implementação
1. **Otimização Final**: Aplique otimizações finais com base nos resultados dos testes
2. **Empacotamento para Implementação**: Empacote modelos e código para implementação na periferia
3. **Documentação**: Documente os requisitos e configurações de implementação
4. **Configuração de Monitorização**: Prepare monitorização e registo para implementação em produção

## Público-Alvo para Desenvolvimento de Edge AI

### Programadores de Edge AI
- Programadores de aplicações que criam dispositivos de periferia e soluções IoT com IA
- Programadores de sistemas embutidos que integram capacidades de IA em dispositivos com restrições de recursos
- Programadores móveis que criam aplicações de IA no dispositivo para smartphones e tablets

### Engenheiros de Edge AI
- Engenheiros de IA que otimizam modelos para implementação na periferia e gerem pipelines de inferência
- Engenheiros de DevOps que implementam e gerem modelos de IA em infraestruturas distribuídas de periferia
- Engenheiros de desempenho que otimizam cargas de trabalho de IA para restrições de hardware na periferia

### Investigadores e Educadores
- Investigadores de IA que desenvolvem modelos e algoritmos eficientes para computação na periferia
- Educadores que ensinam conceitos de Edge AI e demonstram técnicas de otimização
- Estudantes que aprendem sobre os desafios e soluções na implementação de Edge AI

## Casos de Uso de Edge AI

### Dispositivos IoT Inteligentes
- **Reconhecimento de Imagens em Tempo Real**: Implementar modelos de visão computacional em câmaras e sensores IoT
- **Processamento de Voz**: Implementar reconhecimento de fala e processamento de linguagem natural em altifalantes inteligentes
- **Manutenção Preditiva**: Executar modelos de deteção de anomalias em dispositivos industriais de periferia
- **Monitorização Ambiental**: Implementar modelos de análise de dados de sensores para aplicações ambientais

### Aplicações Móveis e Embutidas
- **Tradução no Dispositivo**: Implementar modelos de tradução de linguagem que funcionem offline
- **Realidade Aumentada**: Implementar reconhecimento e rastreamento de objetos em tempo real para aplicações de RA
- **Monitorização de Saúde**: Executar modelos de análise de saúde em dispositivos vestíveis e equipamentos médicos
- **Sistemas Autónomos**: Implementar modelos de tomada de decisão para drones, robôs e veículos

### Infraestrutura de Computação na Periferia
- **Centros de Dados na Periferia**: Implementar modelos de IA em centros de dados na periferia para aplicações de baixa latência
- **Integração com CDN**: Integrar capacidades de processamento de IA em redes de entrega de conteúdo
- **Periferia 5G**: Aproveitar a computação na periferia 5G para aplicações com IA
- **Computação em Névoa**: Implementar processamento de IA em ambientes de computação em névoa

## Instalação e Configuração

### Instalação Rápida
Instale a extensão AI Toolkit diretamente do Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Pré-requisitos para Desenvolvimento de Edge AI
- **ONNX Runtime**: Instale o ONNX Runtime para inferência de modelos
- **Ollama** (Opcional): Instale o Ollama para servir modelos localmente
- **Ambiente Python**: Configure o Python com as bibliotecas de IA necessárias
- **Ferramentas de Hardware de Periferia**: Instale ferramentas de desenvolvimento específicas de hardware (CUDA, OpenVINO, etc.)

### Configuração Inicial
1. Abra o VS Code e instale a extensão AI Toolkit
2. Configure fontes de modelos (ONNX, Ollama, fornecedores na nuvem)
3. Configure o ambiente de desenvolvimento local para testes na periferia
4. Configure opções de aceleração de hardware para a sua máquina de desenvolvimento

## Começando com o Desenvolvimento de Edge AI

### Passo 1: Seleção de Modelos
1. Abra a visualização do AI Toolkit na Barra de Atividades
2. Navegue pelo Catálogo de Modelos para modelos compatíveis com a periferia
3. Filtre por tamanho de modelo, formato (ONNX) e características de desempenho
4. Compare modelos utilizando as ferramentas de comparação integradas

### Passo 2: Testes Locais
1. Utilize o Playground para testar modelos selecionados localmente
2. Experimente diferentes prompts e parâmetros
3. Monitorize métricas de desempenho durante os testes
4. Avalie as respostas dos modelos para requisitos de casos de uso na periferia

### Passo 3: Otimização de Modelos
1. Utilize as ferramentas de Conversão de Modelos para otimizar para implementação na periferia
2. Aplique quantização para reduzir o tamanho do modelo
3. Teste modelos otimizados para garantir desempenho aceitável
4. Documente configurações de otimização e compromissos de desempenho

### Passo 4: Desenvolvimento de Agentes
1. Utilize o Agent Builder para criar agentes de IA otimizados para a periferia
2. Desenvolva prompts que funcionem eficazmente com modelos menores
3. Integre ferramentas e APIs necessárias para cenários de periferia
4. Teste agentes em condições simuladas de periferia

### Passo 5: Avaliação e Implementação
1. Utilize avaliação em lote para testar múltiplas configurações
2. Perfilar desempenho sob várias condições
3. Prepare pacotes de implementação para dispositivos de periferia alvo
4. Configure monitorização e registo para implementação em produção

## Melhores Práticas para Desenvolvimento de Edge AI

### Seleção de Modelos
- **Restrições de Tamanho**: Escolha modelos que se ajustem às limitações de memória dos dispositivos alvo
- **Velocidade de Inferência**: Priorize modelos com tempos de inferência rápidos para aplicações em tempo real
- **Compromissos de Precisão**: Equilibre a precisão do modelo com as restrições de recursos
- **Compatibilidade de Formato**: Prefira formatos ONNX ou otimizados para hardware para implementação na periferia

### Técnicas de Otimização
- **Quantização**: Utilize quantização INT8 ou INT4 para reduzir o tamanho do modelo e melhorar a velocidade
- **Poda**: Remova parâmetros desnecessários do modelo para reduzir requisitos computacionais
- **Destilação de Conhecimento**: Crie modelos menores que mantenham o desempenho de modelos maiores
- **Aceleração de Hardware**: Aproveite NPUs, GPUs ou aceleradores especializados quando disponíveis

### Fluxo de Trabalho de Desenvolvimento
- **Testes Iterativos**: Teste frequentemente em condições semelhantes à periferia durante o desenvolvimento
- **Monitorização de Desempenho**: Monitorize continuamente o uso de recursos e a velocidade de inferência
- **Controlo de Versões**: Acompanhe versões de modelos e configurações de otimização
- **Documentação**: Documente todas as decisões de otimização e compromissos de desempenho

### Considerações de Implementação
- **Monitorização de Recursos**: Monitorize memória, CPU e consumo de energia em produção
- **Estratégias de Fallback**: Implemente mecanismos de fallback para falhas de modelos
- **Mecanismos de Atualização**: Planeie atualizações de modelos e gestão de versões
- **Segurança**: Implementar medidas de segurança adequadas para aplicações de IA na periferia

## Integração com Frameworks de IA na Periferia

### ONNX Runtime
- **Implementação Multiplataforma**: Implementar modelos ONNX em diferentes plataformas de periferia
- **Otimização de Hardware**: Aproveitar as otimizações específicas de hardware do ONNX Runtime
- **Suporte a Dispositivos Móveis**: Utilizar ONNX Runtime Mobile para aplicações em smartphones e tablets
- **Integração com IoT**: Implementar em dispositivos IoT utilizando distribuições leves do ONNX Runtime

### Windows ML
- **Dispositivos Windows**: Otimizar para dispositivos de periferia e PCs baseados em Windows
- **Aceleração NPU**: Aproveitar as Unidades de Processamento Neural em dispositivos Windows
- **DirectML**: Utilizar DirectML para aceleração em GPU nas plataformas Windows
- **Integração UWP**: Integrar com aplicações da Universal Windows Platform

### TensorFlow Lite
- **Otimização para Dispositivos Móveis**: Implementar modelos TensorFlow Lite em dispositivos móveis e incorporados
- **Delegados de Hardware**: Utilizar delegados de hardware especializados para aceleração
- **Microcontroladores**: Implementar em microcontroladores utilizando TensorFlow Lite Micro
- **Suporte Multiplataforma**: Implementar em sistemas Android, iOS e Linux incorporado

### Azure IoT Edge
- **Híbrido Nuvem-Periferia**: Combinar treino na nuvem com inferência na periferia
- **Implementação de Módulos**: Implementar modelos de IA como módulos do IoT Edge
- **Gestão de Dispositivos**: Gerir dispositivos de periferia e atualizações de modelos remotamente
- **Telemetria**: Recolher dados de desempenho e métricas de modelos das implementações na periferia

## Cenários Avançados de IA na Periferia

### Implementação de Múltiplos Modelos
- **Conjuntos de Modelos**: Implementar múltiplos modelos para maior precisão ou redundância
- **Testes A/B**: Testar diferentes modelos simultaneamente em dispositivos de periferia
- **Seleção Dinâmica**: Escolher modelos com base nas condições atuais do dispositivo
- **Partilha de Recursos**: Otimizar o uso de recursos entre vários modelos implementados

### Aprendizagem Federada
- **Treino Distribuído**: Treinar modelos em vários dispositivos de periferia
- **Preservação de Privacidade**: Manter os dados de treino localmente enquanto partilha melhorias nos modelos
- **Aprendizagem Colaborativa**: Permitir que os dispositivos aprendam com experiências coletivas
- **Coordenação Periferia-Nuvem**: Coordenar o treino entre dispositivos de periferia e infraestrutura na nuvem

### Processamento em Tempo Real
- **Processamento de Fluxos**: Processar fluxos contínuos de dados em dispositivos de periferia
- **Inferência de Baixa Latência**: Otimizar para uma latência mínima na inferência
- **Processamento em Lote**: Processar lotes de dados de forma eficiente em dispositivos de periferia
- **Processamento Adaptativo**: Ajustar o processamento com base nas capacidades atuais do dispositivo

## Resolução de Problemas no Desenvolvimento de IA na Periferia

### Problemas Comuns
- **Restrições de Memória**: Modelo demasiado grande para a memória do dispositivo alvo
- **Velocidade de Inferência**: Inferência do modelo demasiado lenta para requisitos em tempo real
- **Degradação de Precisão**: Otimização reduz a precisão do modelo de forma inaceitável
- **Compatibilidade de Hardware**: Modelo incompatível com o hardware alvo

### Estratégias de Depuração
- **Perfil de Desempenho**: Utilizar as funcionalidades de rastreamento do AI Toolkit para identificar gargalos
- **Monitorização de Recursos**: Monitorizar o uso de memória e CPU durante o desenvolvimento
- **Testes Incrementais**: Testar otimizações de forma incremental para isolar problemas
- **Simulação de Hardware**: Utilizar ferramentas de desenvolvimento para simular o hardware alvo

### Soluções de Otimização
- **Quantização Adicional**: Aplicar técnicas de quantização mais agressivas
- **Arquitetura de Modelo**: Considerar diferentes arquiteturas de modelo otimizadas para a periferia
- **Otimização de Pré-processamento**: Otimizar o pré-processamento de dados para restrições da periferia
- **Otimização de Inferência**: Utilizar otimizações de inferência específicas de hardware

## Recursos e Próximos Passos

### Documentação
- [Guia de Modelos do AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/models)
- [Documentação do Model Playground](https://code.visualstudio.com/docs/intelligentapps/playground)
- [Documentação do ONNX Runtime](https://onnxruntime.ai/)
- [Documentação do Windows ML](https://docs.microsoft.com/en-us/windows/ai/)

### Comunidade e Suporte
- [GitHub do VS Code AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)
- [Comunidade ONNX](https://github.com/onnx/onnx)
- [Comunidade de Desenvolvedores de IA na Periferia](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [Marketplace de Extensões do VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Recursos de Aprendizagem
- [Curso de Fundamentos de IA na Periferia](./Module01/README.md)
- [Guia de Modelos de Linguagem Pequenos](./Module02/README.md)
- [Estratégias de Implementação na Periferia](./Module03/README.md)
- [Desenvolvimento de IA na Periferia com Windows](./windowdeveloper.md)

## Conclusão

O AI Toolkit para Visual Studio Code oferece uma plataforma abrangente para o desenvolvimento de IA na periferia, desde a descoberta e otimização de modelos até à implementação e monitorização. Ao aproveitar as suas ferramentas e fluxos de trabalho integrados, os desenvolvedores podem criar, testar e implementar aplicações de IA que funcionam de forma eficiente em dispositivos de periferia com recursos limitados.

O suporte do toolkit para ONNX, Ollama e vários fornecedores de nuvem, combinado com as suas capacidades de otimização e avaliação, torna-o uma escolha ideal para o desenvolvimento de IA na periferia. Quer esteja a construir aplicações IoT, funcionalidades de IA móvel ou sistemas de inteligência incorporada, o AI Toolkit fornece as ferramentas e fluxos de trabalho necessários para uma implementação bem-sucedida de IA na periferia.

À medida que a IA na periferia continua a evoluir, o AI Toolkit para VS Code mantém-se na vanguarda, oferecendo aos desenvolvedores ferramentas e capacidades de ponta para construir a próxima geração de aplicações inteligentes na periferia.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.