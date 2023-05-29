import streamlit as st

e = RuntimeError('This is an exception of type RuntimeError')

st.exception(e)

st.warning('This is a warning', icon="⚠️")

st.error('This is an error', icon="🚨")

st.snow()

st.balloons()