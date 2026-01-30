# Resources Directory

This directory is where you put your documents for the RAG (Retrieval-Augmented Generation) system.

## Requirements

- **Minimum 5 documents** - You must add at least 5 documents
- **Supported formats** - `.txt` and `.pdf` files
- **Your own content** - Use documents relevant to your chosen application

## What to Put Here

Add documents that will serve as the knowledge base for your assistant. Examples:

- Text files (`.txt`) - Plain text documents, notes, guides
- PDF files (`.pdf`) - Articles, manuals, formatted documents

## Tips

1. **Choose focused content** - Documents should be relevant to your application domain
2. **Include variety** - Different aspects of your topic improve retrieval
3. **Check encoding** - Text files should be UTF-8 encoded
4. **Reasonable size** - Very large documents will be chunked automatically

## Testing Your Documents

After adding documents, verify they load correctly:

```bash
python -m ai_in_loop.cli chat
```

Then ask a question that should trigger a document search.

---

**Note:** Delete this README.md after adding your documents, or keep it - it won't affect the retriever since it has a .md extension instead of .txt or .pdf.
