import sys

def redirect_stderr_stdout(stderr=sys.stderr):
    def wrap(f):
        def newf(*args, **kwargs):
            old_stderr = sys.stderr
            sys.stderr = stderr
            try:
                return f(*args, **kwargs)
            finally:
                sys.stderr = old_stderr

        return newf
    return wrap
