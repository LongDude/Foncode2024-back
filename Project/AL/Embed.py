import torch
from transformers import BertModel, BertTokenizerFast

def get_embeddigs(sentences):
    """_summary_

    Args:
        sentences (list(str)): _description_

    Returns:
        numpy_matrix: _description_
    """
    tokenizer = BertTokenizerFast.from_pretrained("setu4993/LaBSE")
    model = BertModel.from_pretrained("setu4993/LaBSE")
    model = model.eval()
    
    inputs = tokenizer(sentences, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    embeddings = outputs.pooler_output
    return embeddings