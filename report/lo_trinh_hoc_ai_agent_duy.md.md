# Lộ Trình Toàn Diện Học Và Phát Triển AI Agent (2025 - 2026)

Tài liệu được biên soạn dành cho **Duy**, cập nhật xu hướng công nghệ Agentic AI mới nhất (LangGraph, CrewAI, AutoGen/AG2, OpenAI Agents SDK, Model Context Protocol - MCP).

---

## 1. Tổng Quan: AI Agent Là Gì?
AI Agent không chỉ dừng lại ở việc phản hồi hội thoại (Chatbot thông thường), mà là một hệ thống tự hành có khả năng:
* **Perceive (Cảm nhận):** Thu nhận input, dữ liệu và ngữ cảnh từ môi trường.
* **Reason (Suy luận & Lập kế hoạch):** Phân rã mục tiêu lớn thành chuỗi tác vụ con (Task decomposition).
* **Act (Hành động):** Sử dụng công cụ (API, database, web search, sandbox code).
* **Reflect & Iterate (Phản tư & Sửa lỗi):** Đánh giá kết quả hành động và tự sửa lỗi đến khi hoàn thành mục tiêu.

---

## 2. Lộ Trình Chi Tiết Theo Từng Giai Đoạn

### Giai đoạn 1: Nền tảng cốt lõi & LLM Foundations (Tuần 1 - 3)
* **Python chuyên sâu cho AI:**
  * Lập trình Hướng đối tượng (OOP) & Bất đồng bộ (`asyncio`, `aiohttp`).
  * Xử lý dữ liệu và schema validation: `Pydantic v2`.
  * Xây dựng Microservices/API: `FastAPI`.
* **LLM Core Concepts:**
  * Context Window, Tokenizer, System Prompt, Temperature, Top-p.
  * Làm việc trực tiếp với SDK của OpenAI, Google Gemini, Anthropic Claude.
* **Agentic Prompting & Function Calling:**
  * Tư duy Agent: Mẫu hình **ReAct** (Reason + Act).
  * Kỹ thuật gọi hàm (Function Calling / Tool Use) với đầu ra chuẩn hóa JSON Schema.

### Giai đoạn 2: Trí nhớ (Memory) & Dữ liệu mở rộng (RAG) (Tuần 4 - 6)
* **Vector Databases & Semantic Search:**
  * Hiểu về Embedding Models.
  * Sử dụng các Vector DB: **ChromaDB** (nhanh gọn), **Qdrant** / **Pinecone** (production).
* **Agentic RAG:**
  * Router Retriever: Tự quyết định nguồn tài liệu cần tra cứu.
  * Self-Correction RAG: Agent tự kiểm tra lại câu trả lời từ tài liệu xem có bị "ảo giác" (hallucination) hay không.
* **Hệ thống bộ nhớ (Memory Systems):**
  * Short-term Memory: Quản lý ngữ cảnh theo phiên hội thoại.
  * Long-term Memory: Lưu trữ sở thích cá nhân, tri thức lâu dài qua semantic memory.

### Giai đoạn 3: Frameworks & Kiến trúc Multi-Agent (Tuần 7 - 10)
* **LangGraph (Ưu tiên số 1 cho Production):**
  * Xây dựng Agent dựa trên State Machine (Đồ thị trạng thái: State, Nodes, Edges).
  * Quản lý luồng phức tạp: Vòng lặp phản hồi (Loops), Kiểm tra trạng thái (Checkpointing), Phân nhánh logic (Conditional branching).
* **CrewAI / AutoGen (AG2):**
  * Mô hình hóa theo đội ngũ (Role-playing Agents): Sequential, Hierarchical orchestration.
  * Đặt mục tiêu (Goal), Nhiệm vụ (Task), Phân quyền người quản lý (Manager).
* **OpenAI Agents SDK:**
  * Nắm bắt chuẩn công nghiệp: Agents, Handoffs, Guardrails, Tracing.

### Giai đoạn 4: Chuẩn kết nối MCP & Production Engineering (Tuần 11 - 14)
* **Model Context Protocol (MCP):**
  * Nắm vững chuẩn mở MCP (chuẩn kết nối công cụ giữa Client và LLM do Anthropic khởi xướng, hiện thuộc Linux Foundation).
  * Tích hợp MCP Server với các công cụ: Enterprise DB, File Systems, GitHub API, Slack,...
* **Human-in-the-Loop (HITL):**
  * Cơ chế dừng lại để con người phê duyệt trước các hành động nhạy cảm (thanh toán, gửi mail, xóa database).
* **Observability & Evaluation (Giám sát & Đánh giá):**
  * Giám sát chuỗi suy nghĩ, token cost, trace lỗi: **LangSmith**, **Arize Phoenix**, **Helicone**.
  * Framework đánh giá: **Ragas**, **DeepEval**.

---

## 3. Lộ Trình Dự Án Thực Chiến (Portfolio Projects)

| Cấp độ | Tên Dự Án | Công Nghệ Sử Dụng | Mục Tiêu Đạt Được |
| :--- | :--- | :--- | :--- |
| **Level 1** | Daily Football Digest Agent | Python, Gemini API, Cron/FastAPI | Agent tự tìm tin tức bóng đá (Messi, La Liga,...), lọc thông tin và gửi tóm tắt qua Telegram |
| **Level 2** | Enterprise Doc Assistant | LangChain, ChromaDB, FastAPI | Agent tra cứu tài liệu kỹ thuật có khả năng tự sửa lỗi câu trả lời (Self-RAG) |
| **Level 3** | Automated Market Research Crew | CrewAI, Tavily Search API, Pydantic | Multi-Agent gồm: Researcher, Writer, Fact-Checker tự tạo báo cáo thị trường |
| **Level 4** | Autonomous Customer Support & Action Engine | LangGraph, MCP, LangSmith, Next.js | Hỗ trợ khách hàng, kết nối cơ sở dữ liệu xử lý hoàn tiền, có cơ chế xin duyệt (HITL) |

---

## 4. Tài Nguyên Học Tập Khuyến Nghị
* **Khóa học miễn phí:**
  * DeepLearning.AI: *AI Agents in LangGraph*, *Multi AI Agent Systems with crewAI*.
* **Tài liệu chính thức (Docs):**
  * [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
  * [CrewAI Documentation](https://docs.crewai.com/)
  * [Model Context Protocol Specification](https://modelcontextprotocol.io/)
* **Cộng đồng:** GitHub trending AI Agent projects, Discord của LangChain & CrewAI.