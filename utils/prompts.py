public_prompt = "Context information from multiple sources is below.\n---------------------\n{context_str}\n---------------------\nGiven the information from multiple sources and not prior knowledge, answer the query in a manner that avoids using technical terms or jargon that a general public without legal background might not understand. \nQuery: {query_str}\nAnswer: "
professional_prompt = "Context information from multiple sources is below.\n---------------------\n{context_str}\n---------------------\nGiven the information from multiple sources and not prior knowledge, answer the query using technical terms and legal domain-specific language along with Act names and Article numbers wherever applicable in moderate amount.  \nQuery: {query_str}\nAnswer: "
judgements_prompt = "Context information from multiple court judgments is below.\n---------------------\n{context_str}\n---------------------\nGiven the information from multiple sources and not prior knowledge, answer the query. Ensure the answer includes references to the specific court judgments from which the context is drawn. Give the details of the judgement before answering the query.\nQuery: {query_str}\nAnswer:"
source_prompt = 'Context information from multiple sources is below.\n---------------------\n{context_str}\n---------------------\nGiven the information from multiple sources and not prior knowledge, answer the query. Ensure the answer includes references to the specific source document from which the context is drawn. Give the details of the source before answering the query.\nQuery: {query_str}\nAnswer: '