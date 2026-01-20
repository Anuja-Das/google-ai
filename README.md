# google-ai

### Studio:
https://aistudio.google.com

-------------------------------------------------

### List of models:
https://generativelanguage.googleapis.com/v1beta/models?key=API_KEY

-------------------------------------------------

### Package:
google-genai

-------------------------------------------------

### Model Categories:

1. **Embeddings**
- embedding-gecko-001
- embedding-001
- text-embedding-004
- gemini-embedding-*

*Use case*: converting text into vectors for semantic search, clustering, recommendation, etc.

Not for text generation — don’t use for “chat” or content creation.

2. **Text Generation / Multimodal**
- gemini-2.5-flash
- gemini-2.5-pro
- gemini-2.0-flash
- gemini-2.0-flash-lite
- gemini-flash-latest
- gemini-pro-latest

These support generateContent.

3. **Experimental / Preview Models**
- gemini-3-pro-preview
- gemini-3-flash-preview
- nano-banana-pro-preview

These models are cutting-edge, may have slightly different behavior, good for testing new features.

4. **Image / TTS / Other**
- imagen-4.*
- veo-*

Ignore unless you want image generation or TTS.
