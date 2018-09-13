import './css/app.css'
import React, { Component } from 'react';
import {index_request} from './api/request'
import { List, Avatar } from 'antd';
import { Card } from 'antd';

const { Meta } = Card;

const data = [
  {
    title: 'Ant Design Title 1',
  },
  {
    title: 'Ant Design Title 2',
  },
  {
    title: 'Ant Design Title 3',
  },
  {
    title: 'Ant Design Title 4',
  },
];

class App extends Component {
  constructor(props) {
    super(props) 
    this.state = {

    }
  }
  componentWillMount() {
    index_request()
  }
  render() {
    return (
      <div  className="global">
       <List
          itemLayout="horizontal"
          dataSource={data}
          renderItem={item => (
            <List.Item>
              <List.Item.Meta
                avatar={<Avatar size={64} src={item.avatar} />}
                title={<a href="https://ant.design">{item.title}</a>}
              />
      </List.Item>
    )}
  />
      </div>
    );
  }
}

export default App;





  