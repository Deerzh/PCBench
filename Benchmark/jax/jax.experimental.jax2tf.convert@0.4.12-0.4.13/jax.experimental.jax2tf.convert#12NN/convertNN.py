import jax
from jax.experimental import jax2tf
import jax.numpy as jnp

def sum_of_squares(x):
    return jnp.sum(x ** 2)
jax2tf.convert(sum_of_squares, polymorphic_shapes=None, native_serialization='default', with_gradient=True, enable_xla=True, experimental_native_lowering='default')
