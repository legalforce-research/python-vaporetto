class Token:
    def end(self) -> int: ...
    def n_tags(self) -> int: ...
    def start(self) -> int: ...
    def surface(self) -> str: ...
    def tag(self, index: int) -> str | None: ...

class TokenIterator:
    def __next__(self) -> Token: ...

class TokenList:
    def __getitem__(self, key: int) -> Token: ...
    def __iter__(self) -> TokenIterator: ...
    def __len__(self) -> int: ...

class Vaporetto:
    def __init__(self, model: bytes, predict_tags: bool = False, wsconst: str = '', norm: bool = True) -> None: ...
    @staticmethod
    def create_from_kytea_model(model: bytes, wsconst: str = '', norm: bool = True) -> Vaporetto: ...
    def tokenize(self, text: str) -> TokenList: ...
    def tokenize_to_string(self, text: str) -> str: ...