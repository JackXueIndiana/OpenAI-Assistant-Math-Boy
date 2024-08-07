# OpenAI-Assistant-Math-Boy
The learning material is from here:
~~~
https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?tabs=command-line%2Ctypescript&pivots=programming-language-ai-studio
~~~
After you tried out in AI Studio, you can try the assistant in code. The generated code needs some clean-up and replacement.

When you run the code you should see
~~~
(aksopenai_env) C:\Users\xinxue\aiflight\mslearn-knowledge-mining\assitant>python testme.py
SyncCursorPage[Message](data=[Message(id='msg_RqtTKkkcBIewnOPeVfwpi7ky', assistant_id='asst_O6PVlMi79WR88tTFJw0PWeSr', attachments=[], completed_at=None, content=[TextContentBlock(text=Text(annotations=[], value='Hello! How can I assist you with math today?'), type='text')], created_at=1723045515, incomplete_at=None, incomplete_details=None, metadata={}, object='thread.message', role='assistant', run_id='run_tAS2PAt5U5ZrufyAg2n3REQx', status=None, thread_id='thread_McYuQjpALVqEj54wxNOmqlUd'), Message(id='msg_W1I3MYBk3EHDPOb8U5bCGg64', assistant_id=None, attachments=[], completed_at=None, content=[TextContentBlock(text=Text(annotations=[], value='Hi, I am your math boy.'), type='text')], created_at=1723045513, incomplete_at=None, incomplete_details=None, metadata={}, object='thread.message', role='user', run_id=None, status=None, thread_id='thread_McYuQjpALVqEj54wxNOmqlUd')], object='list', first_id='msg_RqtTKkkcBIewnOPeVfwpi7ky', last_id='msg_W1I3MYBk3EHDPOb8U5bCGg64', has_more=False)
~~~
