<h1>Qweb Templates Tutorials</h1>
<h2>Lesson 1: Qweb templates Basics</h2>
<h3>There are two types of qweb templates:</h3>
<ol>
    <li><strong>Python Interprater:</strong>
        <p>It only inteperates python expressions</p>
        <p><strong>if you want to use it in python:</strong>
            <ol>
                <li>Define new template:
                    <ol>
                        <li>Use template open and close tags</li>
                        <li>Use name and id properties to define template</li>
                        <li>Between template tags you can write any html script</li>
                        <li>Add this file under data property in manifest file and then upgrade module resulting in two things:
                            <ol>
                                <li>New view will added under qweb views group</li>
                                <li>This view will store in database as recordset</li>
                            </ol>
                        </li>
                    </ol>
                </li>
                <li>Create controller python file:
                    <ol>
                        <li>import http from odoo</li>
                        <li>import request from odoo.http</li>
                        <li>create class encabsulate from http.Controller</li>
                        <li>Create function with decorator:
                            <ol>
                                <li>Decorator with attributes:
                                    <ol>
                                        <li>URL in string format</li>
                                        <li>auth in string format:
                                            <ol>
                                                <li>public: for public user</li>
                                                <li>user: for logged user</li>
                                            </ol>
                                        </li>
                                        <li>type in string format:
                                            <ol>
                                                <li>http: for portal and webpages</li>
                                                <li>json: for APIs</li>
                                            </ol>
                                        </li>
                                        <li>website in boolean value:
                                            <ol>
                                                <li>True: if you call website.layout template</li>
                                                <li>False: if you do not call website.layout template</li>
                                            </ol>
                                        </li>
                                    </ol>
                                </li>
                                <li>function that returns:
                                    <ol>
                                        <li>render method from http.request this function accept parameter as:
                                            <ol>
                                                <li>Template external ID as rference in string format</li>
                                                <li>Any data in dictionary</li>
                                            </ol>
                                        </li>
                                    </ol>
                                </li>
                            </ol>
                        </li>
                        <li></li>
                    </ol>
                </li>
            </ol>
        </p>
        <p>
            <strong>It can be used by:</strong>
            <ol>
                <li>PDF Report function</li>
                <li>Rendering Controller</li>
            </ol>
        </p>
    </li>
    <li><strong>JS Interprater:</strong>
        <p>It only inteperates Java script expressions main purpose for web client</p>
        <p><strong>if you want to use it in Javascript:</strong>
            <ol>
                <li>Define new template:
                    <ol>
                        <li>Use templates open and close tags use xml:space='preserve'</li>
                        <li>inside templates tags define your templates using t open and close tags then use t-name as property of t directive</li>
                        <li>Between t tags you can write any html script</li>
                        <li>Add this file under assets property and mapped to right bundle in manifest file and then upgrade module resulting in two things:
                            <ol>
                                <li>Not stored in database</li>
                                <li>It is called when it needed using t-call-assets</li>
                                <li>when it called it shown in browser network tab under lazy file that contents:
                                    <ol>
                                        <li>all js templates called</li>
                                        <li>all public wedgits</li>
                                        <li>all owl components</li>
                                    </ol>
                                </li>
                            </ol>
                        </li>
                    </ol>
                </li>
                <li>Reference this template on python tempate using css selector</li>
                <li>define owl component or public wedgit with the css selector</li>
            </ol>
        </p>
        <p>
            It can be used by:
            <ol>
                <li>Public Wedgit</li>
                <li>OWL Component</li>
            </ol>
        </p>
    </li>
</ol>

<p>it's based on xml that will geberate xml elements to be used in:</p>
<ol>
    <li>PDF Reports</li>
    <li>Web pages</li>
    <li>Portal</li>
    <li>Client side validations</li>
</ol>
<br/>
<p>Inside this XML elemetns we can use dynamic contents coming from:
    <ol>
        <li>PDF function [Python]</li>
        <li>Controller [Python]</li>
        <li>Kanban view [JS]</li>
        <li>Public wedgit [JS]</li>
        <li>OWL component [JS]</li>
    </ol>
</p>
<h2>Lesson 2: Python Interperater Templates startup</h2>
<strong>Steps:</strong>
<strong><i>Step 1</i></strong>
<ol>
    <li>Create template:
        <xmp>
            <template id="somePythonTemplate" name="Some Python template">
                <h1>Qweb template</h1>
            </template>
        </xmp>
    </li>
    <li>Add file to data property in manifest file</li>
    <li>Upgrade module and search on view grouped by qweb for your template</li>
</ol>

