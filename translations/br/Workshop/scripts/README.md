<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-09T11:09:16+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "br"
}
-->
# Scripts do Workshop

Este diretório contém scripts de automação e suporte usados para manter a qualidade e consistência nos materiais do Workshop.

## Conteúdo

| Arquivo | Finalidade |
|---------|------------|
| `lint_markdown_cli.py` | Verifica blocos de código Markdown para identificar padrões obsoletos de comandos do Foundry Local CLI. |
| `export_benchmark_markdown.py` | Executa benchmarks de latência em múltiplos modelos e gera relatórios em Markdown + JSON. |

## 1. Verificador de Padrões do Markdown CLI

O `lint_markdown_cli.py` analisa todos os arquivos `.md` que não sejam traduções em busca de padrões obsoletos do Foundry Local CLI **dentro de blocos de código delimitados** (``` ... ```). Textos explicativos ainda podem mencionar comandos obsoletos para contexto histórico.

### Padrões Obsoletos (Bloqueados Dentro de Blocos de Código)

O verificador bloqueia padrões de CLI obsoletos. Utilize alternativas modernas.

### Substituições Necessárias
| Obsoleto | Use em vez disso |
|----------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script de benchmark + ferramentas do sistema (`Gerenciador de Tarefas`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Códigos de Saída
| Código | Significado |
|--------|-------------|
| 0 | Nenhuma violação detectada |
| 1 | Um ou mais padrões obsoletos encontrados |

### Execução Local
A partir da raiz do repositório (recomendado):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pré-Commit (Opcional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Isso bloqueia commits que introduzem padrões obsoletos.

### Integração com CI
Um workflow do GitHub Action (`.github/workflows/markdown-cli-lint.yml`) executa o verificador em cada push e pull request para os branches `main` e `Reactor`. Jobs com falhas devem ser corrigidos antes da mesclagem.

### Adicionando Novos Padrões Obsoletos
1. Abra o arquivo `lint_markdown_cli.py`.
2. Adicione uma tupla `(regex, suggestion)` à lista `DEPRECATED`. Use uma string bruta e inclua limites de palavra `\b` quando apropriado.
3. Execute o verificador localmente para verificar a detecção.
4. Faça o commit e o push; o CI aplicará a nova regra.

Exemplo de adição:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Permitindo Menções Explicativas
Como apenas blocos de código delimitados são verificados, você pode descrever comandos obsoletos em texto narrativo com segurança. Se *precisar* mostrá-los dentro de um bloco, use um bloco **sem** as três crases (por exemplo, com indentação ou citação) ou reescreva em forma pseudo.

### Ignorando Arquivos Específicos (Avançado)
Se necessário, coloque exemplos legados em um arquivo separado fora do repositório ou renomeie com uma extensão diferente enquanto estiver em rascunho. Ignorar intencionalmente cópias traduzidas é automático (caminhos contendo `translations`).

### Solução de Problemas
| Problema | Causa | Resolução |
|----------|-------|-----------|
| Verificador sinaliza uma linha que você atualizou | Regex muito ampla | Restrinja o padrão com limites de palavra adicionais (`\b`) ou âncoras |
| CI falha, mas local passa | Versão diferente do Python ou alterações não commitadas | Reexecute localmente, garanta uma árvore de trabalho limpa, verifique a versão do Python no workflow (3.11) |
| Precisa ignorar temporariamente | Correção emergencial | Aplique a correção imediatamente após; considere usar um branch temporário e um PR de acompanhamento (evite adicionar opções de ignorar) |

### Justificativa
Manter a documentação alinhada com a interface CLI estável *atual* evita atritos no workshop, reduz confusão para os participantes e centraliza a medição de desempenho por meio de scripts Python mantidos, em vez de subcomandos CLI desatualizados.

---
Mantido como parte da cadeia de ferramentas de qualidade do workshop. Para melhorias (por exemplo, sugestões de correção automática ou geração de relatórios em HTML), abra um issue ou envie um PR.

## 2. Script de Validação de Exemplos

O `validate_samples.py` valida todos os arquivos de exemplo em Python quanto à sintaxe, imports e conformidade com as melhores práticas.

### Uso
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### O que ele verifica
- ✅ Validade da sintaxe Python
- ✅ Presença de imports necessários
- ✅ Implementação de tratamento de erros (modo detalhado)
- ✅ Uso de type hints (modo detalhado)
- ✅ Docstrings em funções (modo detalhado)
- ✅ Links de referência do SDK (modo detalhado)

### Variáveis de Ambiente
- `SKIP_IMPORT_CHECK=1` - Ignorar validação de imports
- `SKIP_SYNTAX_CHECK=1` - Ignorar validação de sintaxe

### Códigos de Saída
- `0` - Todos os exemplos passaram na validação
- `1` - Um ou mais exemplos falharam

## 3. Executor de Testes de Exemplos

O `test_samples.py` executa testes rápidos em todos os exemplos para verificar se eles são executados sem erros.

### Uso
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Pré-requisitos
- Serviço Foundry Local em execução: `foundry service start`
- Modelos carregados: `foundry model run phi-4-mini`
- Dependências instaladas: `pip install -r requirements.txt`

### O que ele testa
- ✅ O exemplo pode ser executado sem erros de runtime
- ✅ A saída necessária é gerada
- ✅ Tratamento adequado de erros em caso de falha
- ✅ Desempenho (tempo de execução)

### Variáveis de Ambiente
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelo a ser usado para testes
- `TEST_TIMEOUT=30` - Tempo limite por exemplo em segundos

### Falhas Esperadas
Alguns testes podem falhar se dependências opcionais não estiverem instaladas (por exemplo, `ragas`, `sentence-transformers`). Instale com:
```bash
pip install sentence-transformers ragas datasets
```

### Códigos de Saída
- `0` - Todos os testes passaram
- `1` - Um ou mais testes falharam

## 4. Exportador de Benchmark em Markdown

Script: `export_benchmark_markdown.py`

Gera uma tabela de desempenho reproduzível para um conjunto de modelos.

### Uso
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Saídas
| Arquivo | Descrição |
|---------|-----------|
| `benchmark_report.md` | Tabela em Markdown (média, p95, tokens/seg, primeiro token opcional) |
| `benchmark_report.json` | Array de métricas brutas para comparação e histórico |

### Opções
| Flag | Descrição | Padrão |
|------|-----------|--------|
| `--models` | Aliases dos modelos separados por vírgula | (obrigatório) |
| `--prompt` | Prompt usado em cada rodada | (obrigatório) |
| `--rounds` | Rodadas por modelo | 3 |
| `--output` | Arquivo de saída em Markdown | `benchmark_report.md` |
| `--json` | Arquivo de saída em JSON | `benchmark_report.json` |
| `--fail-on-empty` | Saída diferente de zero se todos os benchmarks falharem | desativado |

A variável de ambiente `BENCH_STREAM=1` adiciona a medição de latência do primeiro token.

### Notas
- Reutiliza `workshop_utils` para inicialização e cache consistentes dos modelos.
- Se executado de um diretório de trabalho diferente, o script tenta localizar `workshop_utils` com caminhos alternativos.
- Para comparação de GPU: execute uma vez, habilite aceleração via configuração CLI, reexecute e compare o JSON.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante estar ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.