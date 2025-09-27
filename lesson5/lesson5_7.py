from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import gradio as gr

# 初始化模型
model = OllamaLLM(model="llama3.2:latest")

# 建立多變數的翻譯模板
complex_template = """
你是一位專業的{target_language}翻譯家，專精於{domain}領域。
請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣和風格
2. 使用專業術語
3. 符合{target_language}的語言習慣

{source_language}文本：{text}
{target_language}翻譯：
"""

chat_prompt_template = ChatPromptTemplate.from_template(complex_template)

def translate_text(source_text, source_language, target_language, domain):
    """
    翻譯函數，供Gradio介面使用
    """
    if not source_text.strip():
        return "請輸入要翻譯的文字"
    
    try:
        # 格式化提示詞
        formatted_prompt = chat_prompt_template.format(
            target_language=target_language,
            source_language=source_language,
            domain=domain,
            text=source_text
        )
        
        # 呼叫模型進行翻譯
        response = model.invoke(formatted_prompt)
        return response
    except Exception as e:
        return f"翻譯時發生錯誤：{str(e)}"

# 建立Gradio介面
def create_gradio_interface():
    """
    建立Gradio網頁介面
    """
    with gr.Blocks(title="AI翻譯助手", theme=gr.themes.Soft()) as interface:
        gr.Markdown("# 🌍 AI翻譯助手")
        gr.Markdown("使用LangChain + Ollama進行專業翻譯")
        
        with gr.Row():
            with gr.Column():
                source_text = gr.Textbox(
                    label="要翻譯的文字",
                    placeholder="請輸入要翻譯的文字...",
                    lines=5,
                    max_lines=10
                )
                
                source_language = gr.Dropdown(
                    choices=["英文", "中文", "日文", "韓文", "法文", "德文", "西班牙文"],
                    value="英文",
                    label="來源語言"
                )
                
                target_language = gr.Dropdown(
                    choices=["繁體中文", "簡體中文", "English", "日本語", "한국어", "Français", "Deutsch", "Español"],
                    value="繁體中文",
                    label="目標語言"
                )
                
                domain = gr.Dropdown(
                    choices=["商業", "科技", "醫療", "法律", "教育", "文學", "新聞", "一般"],
                    value="商業",
                    label="專業領域"
                )
                
                translate_btn = gr.Button("🚀 開始翻譯", variant="primary")
            
            with gr.Column():
                output_text = gr.Textbox(
                    label="翻譯結果",
                    lines=10,
                    max_lines=15,
                    interactive=False
                )
        
        # 範例按鈕
        gr.Markdown("### 📝 範例文字")
        example_btn = gr.Button("載入範例", variant="secondary")
        
        # 事件處理
        translate_btn.click(
            fn=translate_text,
            inputs=[source_text, source_language, target_language, domain],
            outputs=output_text
        )
        
        example_btn.click(
            fn=lambda: "The quarterly revenue increased by 15% compared to last year.",
            outputs=source_text
        )
        
        # 頁尾
        gr.Markdown("---")
        gr.Markdown("💡 **使用提示**：選擇適當的專業領域可以獲得更好的翻譯效果")
    
    return interface

# 主程式
if __name__ == "__main__":
    print("🚀 啟動AI翻譯助手...")
    print("📱 Gradio介面將在瀏覽器中開啟")
    
    # 建立並啟動Gradio介面
    interface = create_gradio_interface()
    interface.launch(
        server_name="0.0.0.0",  # 允許外部訪問
        server_port=7860,       # 指定端口
        share=False,            # 不建立公開連結
        show_error=True         # 顯示錯誤訊息
    )