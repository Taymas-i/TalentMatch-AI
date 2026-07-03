class RateLimitError(Exception):
    pass

class LLMTimeoutError(Exception):
    pass

class FileParsingError(Exception):
    pass

class HallucinationGuardError(Exception):
    pass