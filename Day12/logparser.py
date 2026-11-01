import shlex

def logparser(line):
        field = []
        line = line.strip()
        field = shlex.split(line)

        return field

def logparserlistcomprehension(line):
        return [field.strip() for field  in shlex.split(line) if field.strip()]
            

sample_log = "  2026-10-31 23:39:00   ERROR   AuthService   'Invalid credentials'  "
print(logparser(sample_log))
print(logparserlistcomprehension(sample_log))