# APNs 增强计划

## 当前状态
- 已实现基于 JWT 与 ES256 的令牌认证。
- 具备基础的 alert 负载构建，支持标题、副标题、正文、声音与角标。
- 提供同步 HTTP/2 客户端，可单发或列表发送，但头部与负载能力有限。

## 目标
- 提供覆盖 Apple 文档的完整 APNs 客户端，涵盖推送类型、头部、负载、传递选项与环境选择。
- 提供易用且具备类型约束的头部与负载构建器，同时保留底层可配置能力。
- 支持同步与异步发送，具备连接复用、重试与幂等能力。
- 提供清晰的错误处理、可观测性钩子与测试覆盖，且不嵌入密钥或注释。

## 功能待办
### 认证与会话管理
- JWT 缓存与到期前刷新；支持密钥轮换与多签名密钥。
- 可选的提供者证书支持以兼容旧流程（按需）。
- 同步与异步模式下的 HTTP/2 连接复用与池化；可配置超时与代理。

### 请求头
- 完整头部：apns-push-type、apns-id、apns-expiration、apns-priority、apns-topic、apns-collapse-id、apns-time-sensitive（适用时）、apns-relevance-score 以及不同目标的 push-type 变体。
- 按推送类型校验头部组合（如 background 需 priority 5）。
- 提供 apns-id 生成工具以支持幂等重试。

### 负载构建
- 完整 aps 支持：alert 字典（含 launch-image 与本地化键）、badge、sound（含 critical 字段）、content-available、mutable-content、category、thread-id、target-content-id、interruption-level、relevance-score、stale-date、filter-criteria、event-timestamp（适用场景）。
- 支持 Live Activity 更新（含事件时间与过期）与通信类通知。
- 允许 aps 外自定义数据，同时校验大小与 UTF-8 合法性。
- 为 background、VoIP、file provider、complication、location、mdm、push-to-talk 等场景提供专用负载构建。

### 发送接口
- 常用场景的高级方法（alert、background、Live Activity 更新）与低级 send 接口。
- 批量发送支持有界并发与重试策略（5xx、429、空闲连接重置等）。
- 为所有发送方法提供 httpx.AsyncClient 异步版本。
- 可按请求或客户端选择生产/沙箱环境。

### 错误处理与可观测性
- 将 APNs 错误原因映射为具象异常并给出可操作信息。
- 结构化日志钩子与可选指标回调，涵盖成功/失败、延迟与重试计数。
- 捕获并暴露 apns-id 便于追踪，并向调用方提供响应头。

### 校验与安全
- 发送前校验：负载大小、必需头部、推送类型约束与声音文件命名规则。
- 输入净化，避免无效 JSON 与异常头部注入。

### 文档与示例
- 英文 README，涵盖快速上手、高级用法与故障排查。
- 示例覆盖 alert、background、Live Activity、VoIP、批量发送与重试。
- 版本与更新日志，确保 API 稳定性记录。

## 架构规划
- **auth**：JWT 生成与缓存、密钥轮换、可选证书支持。
- **headers**：不可变头部构建器，按推送类型校验，并提供幂等工具。
- **payload**：具类型约束的 aps 与自定义数据构建器，含校验。
- **client**：同步与异步客户端，管理 httpx 会话、重试与批量。
- **errors**：异常类型与错误原因映射。
- **types**：推送类型、打断级别、分类等枚举。
- **config**：超时、代理、重试、环境与遥测钩子的配置对象。

## 测试策略
- 头部与负载构建器的单元测试，覆盖校验与大小限制。
- 使用 httpx 测试工具的模拟 HTTP 测试，验证请求构造、重试与错误处理。
- 可配置端点的集成桩，用于模拟 APNs 响应。
- 对打包元数据的静态检查与最小化的 lint。

## 交付路线
- **Milestone 1**：重构模块（auth、headers、payload、client、errors、types、config）；增加校验与具类型的头部/负载构建器；保持向后兼容的工具方法。
- **Milestone 2**：实现同步/异步客户端，含重试、批量、apns-id 生成与环境覆盖；扩充测试。
- **Milestone 3**：完善专用负载支持（Live Activity、background、VoIP、file provider、mdm）、可观测性钩子与文档。
- **Milestone 4**：补充示例、更新日志与发布流程，准备语义化版本发布。
