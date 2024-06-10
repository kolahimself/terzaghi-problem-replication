import streamlit as st
import method as methods

st.title("Terzaghi's Bearing Factor $N_q$: Problem Replication")
st.write("")

# Trig validation
st.markdown("Trigonometric functions have been configured to work in degrees, for example:")
theta = methods.methods["check"](st.text_input(label="$sin$", key='A1'))
sin_theta = methods.methods["sin"](theta)
st.markdown(f"$sin({theta}) = {sin_theta}$")


st.write("")
phi = int(st.slider(label=r"Supply the value of $\phi$ in degrees",
	min_value=0, max_value=50, value=0, step=1))
# phi = methods.methods["check"](st.text_input(r"Supply the value of $\phi$ in degrees"))
st.write("")

# Nq
nq = methods.methods["Nq"](phi)[0]
numerator = methods.methods["Nq"](phi)[1]
denominator = methods.methods["Nq"](phi)[2]
nq_tab_vals = methods.methods["nq_from_table"](phi)
st.header(r"Calculated N_q")
st.write(f"""
	$$
	N_q = {nq}
	$$""")

st.header(r"N_q from the table values")
st.write(f"""
	$$
	N_q = {nq_tab_vals}
	$$
	""")

# Breakdown
st.header("Breakdown")
breakdown_nq_a = r'''
	$$
	N_q = \frac{e^{2(\frac{3\pi}{4} - \frac{\phi}{2})tan\phi}}{2cos^2(45 + \frac{\phi}{2})} 
	$$''' 
breakdown_nq_b = fr"""
	$$
	= \frac{{e^{{2(\frac{{3\pi}}{{4}} - \frac{{{phi}}}{{2}})tan({{{phi}}})}}}}{{2cos^2(45 + \frac{{{phi}}}{{2}})}} 
	$$
	"""
breakdown_nq_c = fr"""
	$$
	= \frac{{{numerator}}}{{{denominator}}}
	$$
	"""
breakdown_nq_d = fr"""
	$$
	N_q = {{{nq}}}
	$$"""
breakdown_nq = breakdown_nq_a + breakdown_nq_b + breakdown_nq_c + breakdown_nq_d
st.markdown(breakdown_nq)
