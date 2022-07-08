# ESTree (ts ast) parser (external package)

## Execution from python

```python
import subprocess
cwd = os.path.join(_DIR, '..', 'esparser')
p = subprocess.run(["node", "index.js",
                   f"--f={file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
print(p.stdout.decode('utf-8'))
```
