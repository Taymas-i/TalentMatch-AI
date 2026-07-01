class RateLimitError(Exception):
    pass

class LLMTimeoutError(Exception):
    pass

class InvalidPDFEError(Exception):
    pass

class HallucinationGuardError(Exception):
    pass