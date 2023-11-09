"""
PyDCI Notation

LaTex strings for plots to keep notation consistent
"""

def gen_value_str(
    base: str = '\\lambda',
    sample: int = None,
    idx: int = None, 
    name: float = None,
    iteration: int = None,
    bold: bool = True,
    wrap: bool = True) -> str:
    """
    Generates a LaTeX-formatted parameter/observable string with optional superscripts or subscripts.

    Parameters
    ----------
    base : str, optional
        The base symbol for the parameter, by default '\\lambda'.
    sample: int, optional
        The superscript for the parameter, by default None. If provided, it's enclosed in parentheses.
    param: int, optional
        The subscript for the parameter, by default None.
    name: float, optional
        Name to be used either as a superscript if 'iteration' is provided, or
        as an assignment value, by default None.
    iteration : int, optional
        If provided along with 'name', it indicates the iteration and both are used
        as superscripts, separated by a comma, by default None.
    bold : bool, optional
        If True, the string is wrapped in a LaTeX bold command, by default True.
    wrap : bool, optional
        If True, the string is wrapped in LaTeX math mode, by default True.

    Returns
    -------
    str
        A string with the LaTeX-formatted parameter.

    Examples
    --------
    >>> param()
    '$\lambda$'
    >>> param(base='x', sample=2)
    '$\lambda^{(2)}$'
    >>> param(base='x', param_i=1)
    '$\lambda_{1}$'
    >>> param(base='x', name='MUD')
    '$\lambda^{MUD}$'
    >>> param(base='x', name='MUD', iteration=3)
    '$\lambda^{MUD,3}$'

    Notes
    -----
    The function uses raw f-strings (rf-string) to handle the curly braces which are part of LaTeX syntax.
    """
    param_str = rf'{base}' if not bold else rf'\mathbf{{{base}}}'
    if sample is not None:
        param_str += rf'^{{({sample})}}'
    elif name is not None:
        if isinstance(name, str):
            name = rf'\mathrm{{{name}}}'
        if iteration is not None:
            param_str += rf'^{{{name},{iteration}}}'
        else:
            param_str += rf'^{{{name}}}'

    if idx is not None:
        param_str += rf'_{{{idx}}}'

    return rf'${param_str}$' if wrap else param_str

def gen_dist_str(
    base: str = '\pi',
    name: str = None,
    idx: str = None,
    iteration: str = None,
    arg: str = None,
    wrap: bool = True
) -> str:
    """
    Get LaTeX formatted string for distribution.

    Parameters
    ----------
    base : str, optional
        The base string for the distribution (default: '\\pi').
    name : str, optional
        The name of the distribution (default: None).
    idx : str, optional
        The index string (default: None).
    iteration : str, optional
        The iteration string (default: None).
    arg : str, optional
        The argument string (default: None).
    wrap : bool, optional
        Whether to wrap the LaTeX string in '$' (default: True).

    Returns
    -------
    str
        The LaTeX formatted string for the distribution.

    Examples
    --------
    >>> gen_dist_str()
    '$\\pi$'
    >>> gen_dist_str(name='X', idx='i', iteration=2, arg='x', wrap=False)
    '\\pi_{X}^{(2)}|_{i}(x)'
    >>> gen_dist_str(base='\\theta', idx='j', wrap=False)
    '\\theta|_{j}'
    """
    dist_str = rf'{base}'
    if name is not None:
        if isinstance(name, str):
            name = rf'\mathrm{{{name}}}'
        dist_str += rf'_{{{name}}}'
    if iteration is not None:    
        dist_str += rf'^{{({iteration})}}'
    if idx is not None:
        dist_str += rf'|_{{{idx}}}'
    if arg is not None:
        dist_str += rf'({arg})'
    
    return f"${dist_str}$" if wrap else dist_str

def gen_fun_str(
    base: str = 'Q',
    name: str = None,
    idx: str = None,
    iteration: str = None,
    arg: str = None,
    wrap: bool = True
) -> str:
    """
    Get LaTeX formatted string for function.

    Parameters
    ----------
    base : str, optional
        The base string for the function (default: 'Q').
    name : str, optional
        The name of the function (default: None).
    idx : str, optional
        The index string (default: None).
    iteration : str, optional
        The iteration string (default: None).
    arg : str, optional
        The argument string (default: None).
    wrap : bool, optional
        Whether to wrap the LaTeX string in '$' (default: True).

    Returns
    -------
    str
        The LaTeX formatted string for the function.

    Examples
    --------
    >>> gen_fun_str()
    '$Q$'
    >>> gen_fun_str(name='F', idx='i', iteration=2, arg='x', wrap=False)
    'Q_{F}^{(2)}(x)'
    >>> gen_fun_str(base='f', idx='j', wrap=False)
    'f_{j}'
    """
    fun_str = rf'{base}'
    if name is not None:
        if isinstance(name, str):
            name = rf'\mathrm{{{name}}}'
        fun_str += rf'_{{{name}}}'
    if iteration is not None:
        fun_str += rf'^{{({iteration})}}'
    if arg is not None:
        fun_str += rf'({arg})'
    
    return f"${fun_str}$" if wrap else fun_str

def gen_latex(
    key: str,
    idx: str = None,
    iteration: str = None,
    sample: int = None,
    name: float = None,
    bold: bool = True,
    wrap: bool = True,
    arg: str = None,
) -> str:
    """
    Generate LaTeX formatted string for various components based on the specified key.

    Parameters
    ----------
    key : str
        The key specifying the type of component ('param', 'qoi', 'dist', or 'Q').
    idx : str, optional
        The index string (default: None).
    iteration : str, optional
        The iteration string (default: None).
    sample : int, optional
        The sample number (default: None).
    name : float, optional
        The name of the (default: None).
    bold : bool, optional
        Whether to make the generated string bold (default: True).
    wrap : bool, optional
        Whether to wrap the LaTeX string in '$' (default: True).
    arg : str, optional
        The argument string (default: None).

    Returns
    -------
    str
        The LaTeX formatted string for the specified component.

    Examples
    --------
    >>> gen_latex('param', idx='i', iteration=2, sample=1, name=0.5, bold=False, wrap=False)
    '\\lambda_{i}^{(2)}^{(1)}_{0.5}'
    >>> gen_latex('qoi', idx='j', sample=3, name=1.0, wrap=False)
    'q_{j}^{(3)}_{1.0}'
    >>> gen_latex('dist', name='X', idx='k', arg='x', wrap=False)
    '\\pi_{X}|_{k}(x)'
    >>> gen_latex('Q', name='F', idx='l', iteration=4, arg='y', wrap=False)
    'Q_{F}^{(4)}(y)'
    """
    if isinstance(arg, dict):
        sub_key = arg.pop('key')
        arg['wrap'] = False
        arg = gen_latex(sub_key, **arg)

    if key == 'param':
        return gen_value_str(
            base='\\lambda',
            idx=idx,
            iteration=iteration,
            sample=sample,
            name=name,
            bold=bold,
            wrap=wrap,
        )
    elif key == 'qoi':
        return gen_value_str(
            base='q',
            idx=idx,
            iteration=iteration,
            sample=sample,
            name=name,
            bold=bold,
            wrap=wrap,
        )
    elif key == 'dist':
        return gen_dist_str(
            base='\pi',
            name=name,
            idx=idx,
            iteration=iteration,
            arg=arg,
            wrap=wrap,
        )
    elif key == 'Q':
        return gen_fun_str(
            base='Q',
            name=name,
            idx=idx,
            iteration=iteration,
            arg=arg,
            wrap=wrap,
        )
    else:
        raise ValueError(f"Invalid key: {key}. Valid keys are 'param', 'qoi', 'dist', 'Q'")


def exp_ratio_str(e_r, format_spec=".3f", iteration=None):
    """
    Expected ratio string
    """
    iteration_str = rf"^{{({iteration})}}" if iteration is not None else ""
    return rf"$\mathbb{{E}}(r{iteration_str})$= {e_r:{format_spec}}, "

def kl_str(kl, format_spec=".3f"):
    """
    KL string
    """
    return rf"$\mathrm{{KL}}_{{\mathrm{{DCI}}}}$= {kl:{format_spec}}"