import gradio as gr

def greet(gross):
    return "Hello " + gross + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
