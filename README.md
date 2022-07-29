# Anaconda & igl with docker

## Build

```sh
docker build -t anaconda3d .
```

## Run

```sh
docker run -i -t -p 8888:8888 -v ${PWD}\:/tmp/ anaconda3d /bin/bash -c "/opt/conda/bin/jupyter notebook --notebook-dir=/tmp/ --ip='0.0.0.0' --port=8888 --no-browser --allow-root --NotebookApp.token=toto"
```

## Test

- Run container
- Go to http://localhost:8888
- Open a new Python 3 notebook
- Execute the following code :
```python
import igl
import meshplot as mp
import numpy as np

v, f = igl.read_triangle_mesh("data/teapot.obj")
mp.plot(v, f, v[:, 0])
```

![teapot](teapot.png)

## References

- https://www.anaconda.com/[Anaconda]
- https://github.com/libigl/libigl/[libigl]
- https://geometryprocessing.github.io/geometric-computing-python/viz_basic/[viz_basic]
