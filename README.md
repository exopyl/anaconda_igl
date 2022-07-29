# Anaconda & igl with docker

## Build

```sh
docker build -t anaconda_igl .
```

## Run

```sh
docker run -i -t -p 8888:8888 -v ${PWD}\:/tmp/ anaconda_igl /bin/bash -c "/opt/conda/bin/jupyter notebook --notebook-dir=/tmp/ --ip='0.0.0.0' --port=8888 --no-browser --allow-root --NotebookApp.token=toto"
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
c = np.array([1, 0, 0])
shading = {"flat":True, "wireframe": True, "wire_color": "black", "wire_width": 0.01}
p = mp.plot(v, f, c, shading=shading)
```



## References

- https://www.anaconda.com/
- https://github.com/libigl/libigl/
- https://geometryprocessing.github.io/geometric-computing-python/viz_basic/
- https://skoch9.github.io/meshplot/
