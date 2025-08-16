from abc import ABC , abstractmethod

class LLMInterface(ABC):

    @abstractmethod
    def set_generation_model(self , model_id : str):
        pass

    @abstractmethod
    def set_embedding_model(self , model_id : str):
        pass
    
    @abstractmethod
    def generate_text(self , prompt : str ,
                                max_tokens : int  ,
                                temperature : float,
                                top_p : float = 0.9 ,
                                stop : list = None ,
                                ):
        pass
    @abstractmethod
    def embed_text (self , text : str, document_type: str):
        pass

    
