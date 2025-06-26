# xiaoqiang-MCPx
背景:
给予fastgpt构建的RAG能力，可以提供:

- 针对不同癌种的知识库
- RAG驱动的智能体助手7个和1个罕见病助手
- API能力，webhook（微信，飞书，dingding集成能力）
- mcp工具能力

缺乏

- 搜索能力
- deep research能力

目前可以稳定完成

- 癌症患者的知识科普（医学术语，检测指标，药物使用，基因报告解读）
- 医疗报告解读（病理检测/影像检测/血液检测/基因检测报告解读）

数据合规限制

- 不采集个人身份数据
- 完整的QA数据

# 快速上手

本仓库提供一个简化版的 MCP 服务器示例，可通过以下命令启动：

```bash
python -m src.server.mcp_server
```

在启动后，可按照 JSON-RPC 2.0 的格式向服务器发送请求，调用示例工具 `query_knowledge_base`、`query_medical_resources`、`analyze_report`、`query_clinical_trials`、`plan_travel`、`query_insurance_policy` 或 `query_drug_info`。

### 列出服务器提供的工具

```json
{"jsonrpc": "2.0", "id": "1", "method": "tools/list", "params": {}}
```

### 获取服务器能力声明

```json
{"jsonrpc": "2.0", "id": "2", "method": "server/get_capabilities", "params": {}}
```

`server/get_capabilities` 的返回值来源于 `config/capabilities.json`，若该文件不存在或解析失败，将使用内置的默认能力声明。

# mcp的设计想法

1. 通过mcp，让现有能力可以开放给更多开发者和开源社区应用
2. 个人感觉：知识库，相比RAG智能体，可能更多人关心
3. MCP的tools构成
   - 知识库查询
   - 医疗资源查询
   - 报告分析
   - 临床试验查询
   - 就医旅行规划
   - 医保政策咨询
   - 药物信息查询

---

## 需要讨论的问题

### 1. 目标用户定位

- [x] 主要面向开发者还是最终用户？ - **开发者和专业背景的患者**
- [x] 是否需要考虑不同技术水平的用户？ - **降到最低**
- [x] 对于医疗专业性要求如何平衡？ - **平衡，但是不要求专业**

### 2. 功能优先级

- [x] 哪些工具是MVP必须包含的？ - **知识库，医疗资源，报告分析，临床试验查询**
- [x] 哪些功能可以在后续版本中添加？ - **服务类比如医保咨询**
- [x] 用户最迫切需要的功能是什么？ - **知识库，找靠谱的医院和医生，合理的治疗策略，以及临床试验**

### 3. 技术架构选择

- [x] 选择什么编程语言和框架？ - **MCP标准开放框架**
- [x] 如何处理外部API的依赖和稳定性？ - **12306，高德地图，丁香园，百度这些开放API可以调用**
- [x] 数据缓存和性能优化策略？ - **一般**

### 4. 数据安全和合规

- [x] 除了不采集个人身份数据，还有哪些合规要求？ - **没了**
- [x] 如何确保医疗信息的准确性和时效性？ - **数据来源都是公开的，比如12306，丁香园，百度等**
- [x] 错误信息的免责声明如何设计？ - **已经有了**

### 5. 商业模式

- [x] 完全开源还是部分收费？ - **开源免费**
- [x] API调用限制和计费方式？ - **设定防止被滥用，但是不收费**
- [x] 如何可持续发展？ - **社区维护，统一进行开发**

## MVP实施计划

基于以上讨论结果，制定以下实施计划：

### 第一阶段：核心工具开发（MVP）

#### 1. 知识库查询工具

- **功能**：针对不同癌种的专业知识查询
- **输入**：癌症类型、查询关键词
- **输出**：相关医学知识、治疗方案、注意事项
- **数据源**：现有fastgpt知识库

#### 2. 医疗资源查询工具

- **功能**：查找靠谱的医院和医生
- **输入**：疾病类型、地理位置、医院等级要求
- **输出**：推荐医院列表、医生信息、科室介绍
- **数据源**：公开医院数据库、医生执业信息

#### 3. 医疗报告分析工具

- **功能**：解读各类医疗检测报告
- **输入**：报告类型（病理/影像/血液/基因）、报告内容
- **输出**：报告解读、异常指标说明、建议后续行动
- **技术**：基于现有RAG能力

#### 4. 临床试验查询工具

- **功能**：查找相关临床试验机会
- **输入**：疾病类型、患者条件、地理位置
- **输出**：符合条件的试验列表、入组要求、联系方式
- **数据源**：clinicaltrials.gov官方API

### 第二阶段：扩展功能（已实现）

#### 1. 外地就医旅行规划

- **集成API**：12306（交通）、高德地图（路线规划）
- **功能**：提供完整的就医出行方案

#### 2. 医保政策咨询

- **功能**：查询医保报销政策、药物目录
- **数据源**：各地医保局公开数据

#### 3. 药物查询工具

- **数据源**：丁香园、百度健康等开放API
- **功能**：药物信息、副作用、价格比较

### 技术架构设计

#### MCP标准合规性分析

**✅ 符合MCP标准的设计要素：**

- 客户端-服务器架构分离
- 基于JSON-RPC 2.0通信协议
- 工具(Tools)、资源(Resources)、提示(Prompts)三大核心概念
- 模块化工具暴露机制

**⚠️ 需要标准化的技术实现：**

- 使用官方MCP SDK (`@modelcontextprotocol/sdk`)
- 严格遵循JSON-RPC 2.0消息格式
- 实现标准的能力协商机制
- 加强传输层安全(HTTPS/本地绑定)

#### MCP服务器标准结构

```
小胰宝-MCP服务器/
├── src/
│   ├── server/
│   │   ├── mcp_server.py          # MCP服务器核心(基于官方SDK)
│   │   ├── capabilities.py       # 能力声明和协商
│   │   ├── transport.py           # 传输层(stdio/HTTP-SSE)
│   │   └── message_handler.py     # JSON-RPC消息处理
│   ├── tools/                     # MCP工具实现
│   │   ├── __init__.py
│   │   ├── knowledge_base.py      # 知识库查询工具
│   │   ├── medical_resources.py   # 医疗资源查询工具
│   │   ├── report_analysis.py     # 报告分析工具
│   │   ├── clinical_trials.py     # 临床试验查询工具
│   │   ├── travel_planner.py      # 就医旅行规划工具
│   │   ├── insurance_policy.py    # 医保政策咨询工具
│   │   └── drug_info.py           # 药物信息查询工具
│   ├── resources/                 # MCP资源实现
│   │   ├── __init__.py
│   │   ├── knowledge_db.py        # 知识库资源
│   │   └── medical_data.py        # 医疗数据资源
│   ├── prompts/                   # MCP提示实现
│   │   ├── __init__.py
│   │   └── medical_prompts.py     # 医疗相关提示模板
│   ├── schemas/                   # JSON Schema定义
│   │   ├── tool_schemas.py        # 工具输入输出模式
│   │   └── resource_schemas.py    # 资源模式定义
│   ├── integrations/
│   │   ├── fastgpt_client.py      # FastGPT集成
│   │   ├── clinicaltrials_api.py  # 临床试验API
│   │   └── external_apis.py       # 其他外部API
│   ├── security/
│   │   ├── auth.py                # 认证授权
│   │   ├── rate_limiter.py        # 访问限制
│   │   └── validator.py           # 数据验证
│   └── utils/
│       ├── cache_manager.py       # 缓存管理
│       ├── logger.py              # 日志记录
│       └── error_handler.py       # 错误处理
├── config/
│   ├── mcp_config.json           # MCP标准配置
│   ├── capabilities.json         # 服务器能力声明
│   └── api_keys.env              # API密钥配置
├── docs/
│   ├── README.md                 # 项目说明
│   ├── MCP_COMPLIANCE.md         # MCP标准合规说明
│   ├── API_DOCS.md              # API文档
│   └── DEPLOYMENT.md            # 部署指南
└── tests/
    ├── test_mcp_compliance.py   # MCP标准合规测试
    ├── test_tools.py            # 工具测试
    ├── test_resources.py        # 资源测试
    └── test_integrations.py    # 集成测试
```

#### MCP标准实现细节

**1. 工具定义标准化**

```python
# 示例：知识库查询工具的MCP标准定义
from mcp.types import Tool

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="query_knowledge_base",
            description="查询癌症相关知识库，提供专业医学知识",
            inputSchema={
                "type": "object",
                "properties": {
                    "cancer_type": {
                        "type": "string", 
                        "description": "癌症类型(如：肺癌、乳腺癌等)",
                        "enum": ["肺癌", "乳腺癌", "胃癌", "肝癌", "结直肠癌"]
                    },
                    "query": {
                        "type": "string", 
                        "description": "查询关键词或问题"
                    },
                    "detail_level": {
                        "type": "string",
                        "description": "详细程度",
                        "enum": ["简要", "详细", "专业"]
                    }
                },
                "required": ["cancer_type", "query"]
            }
        )
    ]
```

**2. JSON-RPC 2.0消息处理**

```python
# 标准的MCP消息格式
{
    "jsonrpc": "2.0",
    "id": "request-123",
    "method": "tools/call",
    "params": {
        "name": "query_knowledge_base",
        "arguments": {
            "cancer_type": "肺癌",
            "query": "靶向治疗药物有哪些",
            "detail_level": "详细"
        }
    }
}
```

**3. 能力协商机制**

```python
# 服务器能力声明
server_capabilities = {
    "tools": {"listChanged": True},
    "resources": {"subscribe": True, "listChanged": True},
    "prompts": {"listChanged": True},
    "logging": {}
}
```

**4. 传输层安全实现**

```python
# stdio传输（推荐用于本地部署）
from mcp.server.stdio import StdioServerTransport

async def main():
    # 绑定到localhost确保安全
    transport = StdioServerTransport()
    await server.run(transport)

# HTTPS传输（用于远程部署）
from mcp.server.sse import SseServerTransport

transport = SseServerTransport(
    "/message",
    host="127.0.0.1",  # 仅本地绑定
    port=8080,
    ssl_context=ssl_context  # 必须使用SSL
)
```

#### 防滥用和安全机制

**MCP标准安全要求：**

- **本地绑定**：生产环境绑定到localhost(127.0.0.1)
- **HTTPS强制**：远程连接必须使用TLS/HTTPS
- **会话验证**：实现加密安全的会话ID验证
- **输入验证**：严格的JSON Schema验证

**自定义防滥用策略：**

- **访问频率限制**：每用户每小时最多100次请求
- **IP限制**：单IP每分钟最多10次请求  
- **Token验证**：需要注册获取访问Token
- **使用统计**：记录使用情况，异常检测
- **错误处理**：标准JSON-RPC 2.0错误码

#### MCP合规开发时间线

**第1步：MCP框架搭建**

- 集成官方MCP SDK
- 实现标准JSON-RPC 2.0通信
- 搭建能力协商机制
- 完成知识库查询工具(符合MCP标准)

**第2步：核心工具开发**

- 医疗资源查询工具标准化
- 报告分析工具MCP适配
- JSON Schema定义完善
- 传输层安全实现

**第3步：扩展功能集成**

- 临床试验查询API集成
- 资源(Resources)和提示(Prompts)实现
- 外部API标准化封装

**第4步：安全和测试**

- MCP标准合规测试
- 防滥用机制完善
- 安全传输验证
- 文档编写(包含MCP合规说明)

**第5步：优化和发布**

- 性能优化和缓存机制
- 完整的MCP生态测试
- MVP版本发布
- 社区反馈收集

## 代码质量和可维护性改进建议

### 1. 错误处理机制强化

```python
# MCP标准错误处理
from mcp.types import McpError

class MedicalDataError(McpError):
    """医疗数据相关错误"""
    def __init__(self, message: str, code: int = -32000):
        super().__init__(code, message)

# 统一错误处理装饰器
def handle_mcp_errors(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ValidationError as e:
            raise McpError(-32602, f"参数验证失败: {e}")
        except APIError as e:
            raise McpError(-32603, f"外部API调用失败: {e}")
        except Exception as e:
            logger.error(f"未预期错误: {e}")
            raise McpError(-32603, "内部服务器错误")
    return wrapper
```

### 2. 数据验证增强

```python
# 使用Pydantic进行严格的数据验证
from pydantic import BaseModel, validator

class KnowledgeQueryRequest(BaseModel):
    cancer_type: str
    query: str
    detail_level: str = "详细"
    
    @validator('cancer_type')
    def validate_cancer_type(cls, v):
        allowed_types = ["肺癌", "乳腺癌", "胃癌", "肝癌", "结直肠癌"]
        if v not in allowed_types:
            raise ValueError(f"不支持的癌症类型: {v}")
        return v
    
    @validator('query')
    def validate_query(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("查询内容不能少于2个字符")
        return v.strip()
```

### 3. 性能优化策略

```python
# 智能缓存机制
import asyncio
from functools import wraps
from typing import Dict, Any

class MCPCache:
    def __init__(self, ttl: int = 3600):
        self.cache: Dict[str, Any] = {}
        self.ttl = ttl
    
    async def get_or_set(self, key: str, func, *args, **kwargs):
        if key in self.cache:
            return self.cache[key]
        
        result = await func(*args, **kwargs)
        self.cache[key] = result
        
        # 异步清理过期缓存
        asyncio.create_task(self._expire_key(key))
        return result
    
    async def _expire_key(self, key: str):
        await asyncio.sleep(self.ttl)
        self.cache.pop(key, None)

# 缓存装饰器
def cached_tool(ttl: int = 3600):
    def decorator(func):
        cache = MCPCache(ttl)
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            return await cache.get_or_set(cache_key, func, *args, **kwargs)
        return wrapper
    return decorator
```

### 4. 监控和运维

```python
# 结构化日志记录
import structlog
from datetime import datetime

logger = structlog.get_logger()

class MCPMetrics:
    def __init__(self):
        self.tool_calls = {}
        self.error_counts = {}
        self.response_times = []
    
    def record_tool_call(self, tool_name: str, duration: float, success: bool):
        # 记录工具调用统计
        if tool_name not in self.tool_calls:
            self.tool_calls[tool_name] = {"count": 0, "success": 0, "avg_time": 0}
        
        self.tool_calls[tool_name]["count"] += 1
        if success:
            self.tool_calls[tool_name]["success"] += 1
        
        # 记录响应时间
        self.response_times.append(duration)
        
        # 结构化日志
        logger.info(
            "tool_call_completed",
            tool_name=tool_name,
            duration=duration,
            success=success,
            timestamp=datetime.now().isoformat()
        )
```

### 5. 文档完善

```python
# 自动生成MCP工具文档
from typing import get_type_hints

def generate_tool_docs(tool_class):
    """自动生成工具的MCP标准文档"""
    docs = {
        "name": tool_class.__name__,
        "description": tool_class.__doc__,
        "methods": [],
        "schemas": {}
    }
    
    for method_name in dir(tool_class):
        if method_name.startswith('tool_'):
            method = getattr(tool_class, method_name)
            hints = get_type_hints(method)
            
            docs["methods"].append({
                "name": method_name,
                "description": method.__doc__,
                "input_schema": hints.get('input', {}),
                "output_schema": hints.get('return', {})
            })
    
    return docs
```

## 下一步实施建议

### 立即开始的工作

1. **环境搭建**：安装MCP官方SDK和开发环境
2. **原型验证**：先实现一个简单的知识库查询工具验证技术路线
3. **标准制定**：建立代码规范、提交规范和测试标准

### 优先实现的模块

1. **知识库查询工具**：作为MCP标准实现的模板
2. **基础框架**：MCP服务器核心、传输层、错误处理
3. **安全机制**：认证、限流、数据验证

### 技术选型建议

- **编程语言**：Python 3.9+ (与现有FastGPT技术栈一致)
- **MCP SDK**：官方Python SDK
- **数据验证**：Pydantic
- **异步框架**：asyncio + aiohttp
- **日志系统**：structlog
- **测试框架**：pytest + pytest-asyncio

### 成功指标

- ✅ 通过MCP官方合规性测试
- ✅ 与Claude Desktop成功集成
- ✅ 工具响应时间 < 2秒
- ✅ 99%的可用性
- ✅ 完整的API文档和使用示例

---
