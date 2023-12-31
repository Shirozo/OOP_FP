class Session:
    _session = None
    
    def __new__(cls) -> object:
        if cls._session is None:
            cls._session = super(Session, cls).__new__(cls)
            cls._session._data = {}
        return cls._session

    def set(self, user : str, id : int, type : int) -> None:
        if self._data:
            return "There's an active session"
        self._data = {
            "username" : user,
            "user_id" : id,
            "user_type" : type
        }
    
    def get(self) -> dict:
        return self._data

    def clear(self) -> None:
        self._data = {}