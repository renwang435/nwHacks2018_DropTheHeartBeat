import React, { Component } from 'react';

const ListItem = props => (
    <ul>
        {props.entries.map((item, index) =>
            <li key={index}>
                {item.text}
                <button value={index} onClick={() => props.remove(item.id)}>x</button>
            </li>
        )}
    </ul>
);



export default ListItem;
