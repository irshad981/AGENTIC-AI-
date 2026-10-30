{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fff2b5b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-10-28 13:25:55.685 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-28 13:25:55.686 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-28 13:25:55.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-28 13:25:55.688 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-28 13:25:55.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-10-28 13:25:55.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Hello, Streamlit!\")\n",
    "st.write(\"If you can read this in your browser, Streamlit is working.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6b1b91af",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2147799488.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[9]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mstreamlit run hello_streamlit.py\u001b[39m\n              ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run hello_streamlit.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.13.13)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
