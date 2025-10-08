<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8344ea4f8f563cfa921e09247588a225",
  "translation_date": "2025-10-08T20:59:01+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "pt"
}
-->
# Scripts do Workshop

Este diretório contém scripts de automação e suporte usados para manter a qualidade e consistência nos materiais do Workshop.

## Conteúdo

| Ficheiro | Finalidade |
|----------|------------|
| `lint_markdown_cli.py` | Verifica blocos de código Markdown para padrões obsoletos de comandos Foundry Local CLI. |
| `export_benchmark_markdown.py` | Executa benchmarks de latência multi-modelo e gera relatórios em Markdown + JSON. |

## 1. Verificador de Padrões CLI em Markdown

O `lint_markdown_cli.py` analisa todos os ficheiros `.md` não traduzidos em busca de padrões obsoletos do Foundry Local CLI **dentro de blocos de código delimitados** (``` ... ```). O texto informativo ainda pode mencionar comandos obsoletos para contexto histórico.

### Padrões Obsoletos (Bloqueados Dentro de Blocos de Código)

O verificador bloqueia padrões CLI obsoletos. Utilize alternativas modernas.

### Substituições Necessárias
| Obsoleto | Usar Em Vez |
|----------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script de benchmark + ferramentas do sistema (`Gestor de Tarefas`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Códigos de Saída
| Código | Significado |
|--------|-------------|
| 0 | Nenhuma violação detetada |
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

### Hook de Pré-Commit (Opcional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Este bloqueia commits que introduzem padrões obsoletos.

### Integração com CI
Um workflow do GitHub Action (`.github/workflows/markdown-cli-lint.yml`) executa o verificador em cada push e pull request para as branches `main` e `Reactor`. Jobs com falhas devem ser corrigidos antes da fusão.

### Adicionar Novos Padrões Obsoletos
1. Abra o ficheiro `lint_markdown_cli.py`.
2. Adicione um tuplo `(regex, suggestion)` à lista `DEPRECATED`. Utilize uma string raw e inclua limites de palavra `\b` onde apropriado.
3. Execute o verificador localmente para verificar a deteção.
4. Faça commit e push; o CI aplicará a nova regra.

Exemplo de adição:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Permitir Menções Explicativas
Como apenas blocos de código delimitados são aplicados, pode descrever comandos obsoletos em texto narrativo sem problemas. Se *precisar* de os mostrar dentro de um bloco delimitado para contraste, adicione um bloco delimitado **sem** três acentos graves (por exemplo, indentado ou citado) ou reescreva em forma pseudo.

### Ignorar Ficheiros Específicos (Avançado)
Se necessário, envolva exemplos antigos num ficheiro separado fora do repositório ou renomeie com uma extensão diferente enquanto estiver a trabalhar. Ignorar intencionalmente cópias traduzidas é automático (caminhos que contêm `translations`).

### Resolução de Problemas
| Problema | Causa | Resolução |
|----------|-------|-----------|
| O verificador sinaliza uma linha que atualizou | Regex muito amplo | Restrinja o padrão com limites de palavra adicionais (`\b`) ou âncoras |
| CI falha, mas localmente passa | Versão diferente do Python ou alterações não commitadas | Reexecute localmente, certifique-se de que o diretório de trabalho está limpo, verifique a versão do Python no workflow (3.11) |
| Precisa de ignorar temporariamente | Correção urgente | Aplique a correção imediatamente após; considere usar uma branch temporária e um PR de acompanhamento (evite adicionar opções de ignorar) |

### Justificação
Manter a documentação alinhada com a superfície CLI *atual* e estável evita fricção no workshop, reduz confusão para os participantes e centraliza a medição de desempenho através de scripts Python mantidos em vez de subcomandos CLI desatualizados.

---
Mantido como parte da cadeia de ferramentas de qualidade do workshop. Para melhorias (por exemplo, sugestões de correção automática ou geração de relatórios em HTML), abra um issue ou envie um PR.

## 2. Script de Validação de Exemplos

O `validate_samples.py` valida todos os ficheiros de exemplo Python para conformidade com sintaxe, imports e boas práticas.

### Utilização
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

### O que verifica
- ✅ Validade da sintaxe Python
- ✅ Imports necessários presentes
- ✅ Implementação de tratamento de erros (modo detalhado)
- ✅ Uso de dicas de tipo (modo detalhado)
- ✅ Docstrings de funções (modo detalhado)
- ✅ Links de referência do SDK (modo detalhado)

### Variáveis de Ambiente
- `SKIP_IMPORT_CHECK=1` - Ignorar validação de imports
- `SKIP_SYNTAX_CHECK=1` - Ignorar validação de sintaxe

### Códigos de Saída
- `0` - Todos os exemplos passaram na validação
- `1` - Um ou mais exemplos falharam

## 3. Executor de Testes de Exemplos

O `test_samples.py` executa testes rápidos em todos os exemplos para verificar se são executados sem erros.

### Utilização
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

### O que testa
- ✅ O exemplo pode ser executado sem erros de runtime
- ✅ A saída necessária é gerada
- ✅ Tratamento adequado de erros em caso de falha
- ✅ Desempenho (tempo de execução)

### Variáveis de Ambiente
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelo a usar para testes
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

### Utilização
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Saídas
| Ficheiro | Descrição |
|----------|-----------|
| `benchmark_report.md` | Tabela em Markdown (média, p95, tokens/segundo, opcional primeiro token) |
| `benchmark_report.json` | Array de métricas brutas para comparação e histórico |

### Opções
| Flag | Descrição | Padrão |
|------|-----------|--------|
| `--models` | Aliases de modelos separados por vírgulas | (obrigatório) |
| `--prompt` | Prompt usado em cada rodada | (obrigatório) |
| `--rounds` | Rodadas por modelo | 3 |
| `--output` | Ficheiro de saída em Markdown | `benchmark_report.md` |
| `--json` | Ficheiro de saída em JSON | `benchmark_report.json` |
| `--fail-on-empty` | Saída diferente de zero se todos os benchmarks falharem | desativado |

A variável de ambiente `BENCH_STREAM=1` adiciona medição de latência do primeiro token.

### Notas
- Reutiliza `workshop_utils` para inicialização e cache consistentes de modelos.
- Se executado a partir de um diretório de trabalho diferente, o script tenta caminhos alternativos para localizar `workshop_utils`.
- Para comparação de GPU: execute uma vez, ative aceleração via configuração CLI, reexecute e compare o JSON.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.