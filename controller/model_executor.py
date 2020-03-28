from abc import abstractmethod, ABC

class ModelExecutor(ABC):

    @abstractmethod
    def executeModel(self, request):
            pass