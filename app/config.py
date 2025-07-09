class CompileConfig:
    def __init__(self, mode="fast", show_complexity=True, optimize=True):
        self.mode = mode  # 'fast', 'debug', 'strict'
        self.show_complexity = show_complexity
        self.optimize = optimize

    def __str__(self):
        return f"CompileMode: {self.mode}, ShowComplexity: {self.show_complexity}, Optimize: {self.optimize}"

# Default global config
CONFIG = CompileConfig()
